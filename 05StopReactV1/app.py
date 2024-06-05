from flask import Flask, render_template, request

app = Flask(__name__)

# List of allergens (predefined list of not safe ingredients)
predefined_list = {
    "fragrancemix1_1": ['alpha-amylcinnamaldehyde', 'fragrance', 'perfume', 'amyl cinnamal', 'amylcinnamaldehyde',
                        'cinnamal', 'cinnamaldehyde', 'cinnamic alcohol', 'cinnamic aldehyde', 'cinnamyl alcohol',
                        'eugenol', 'evernia prunastri', 'geraniol', 'hydroxycitronellal', 'isoeugenol', 'oak moss',
                        'oakmoss absolute resin', 'oakmoss concrete', 'oakmoss oil', 'oakmoss extract',
                        'sorbitan sesquioleate', 'coumarin', '2h-1-benzopyran-2-one', 'coumarin [nf x]',
                        'tonka bean camphor', '1,2-benzopyrone', '2-oxo-1,2-benzopyran', '2-oxo', '2-oxo', '2-oxo-1',
                        '2-oxo-1,', 'benzopyran', 'benzopyran', '2-propenoic acid', '3-(2-hydroxyphenyl)',
                        'delta-lactone', 'hydroxyphenyl', 'hydroxyphenyl', '3-(2-hydroxyphenyl)propenoic acid',
                        '3-(2-hydroxyphenyl)propenoic acid2-propenoic acid', 'propenoic acid', 'propenoic acid',
                        '3-(2-hydroxyphenyl)-delta-lactone', '2h-1-benzopyran, 2-oxo-', '2h-1-benzopyran-2-one',
                        '2h-benzo(b)pyran-2-one', '3-(2-hydroxyphenyl)-2-propenoic delta-lactone', '5,6-benzo-alpha-pyrone',
                        '5-17-10-00143', 'ai3-00753', 'brn 0383644', '0383644benzo-alpha-pyrone', 'ccris 181',
                        'caswell no. 259c', '259c', 'cinnamic acid', 'o-hydroxy-', 'hydroxy', 'delta-lactone', 'coumarin',
                        'coumarinic anhydride', 'coumarinic lactone', 'cumarin', 'einecs 202-086-7', '202-086-7',
                        '127301', 'rattex', 'tonka bean camphor', 'cis-o-coumaric acid anhydride',
                        'cis-o-coumarinic acid lactone', 'o-coumaric acid lactone'],
    "fragrancemix1_2": ['o-hydroxycinnamic acid lactone', 'o-hydroxycinnamic lactone',
                        '4-(4-hydroxy-4-methylpentyl)-3-cyclohexene-1-carboxaldehyde', 'brn 2046455',
                        'einecs 250-863-4', '3-cyclohexene-1-carboxaldehyde, 4-(4-hydroxy-4-methylpentyl)-',
                        '4-(4-hydroxy-4-methylpentyl)cyclohex-3-enecarbaldehyde',
                        '3-cyclohexene-1-carboxaldehyde, 4-(4-hydroxy-4-methylpentyl)-', '2,6-dimethyl-2-octen-8-ol',
                        '3,7-dimethyl-6-octen-1-ol', '4-01-00-02188 (beilstein handbook reference)', 'ai3-25080',
                        'brn 1721507', 'ccris 7452', 'cephrol', 'citronellol (ex. java citronella oil) (natural)',
                        'citronellol (natural)', 'einecs 203-375-0', 'elenol', 'fema no. 2309', 'nsc 8779', 'rhodinol',
                        'rodinol', '2,6,10-dodecatrien-1-ol, 3,7,11-trimethyl-',
                        '3,7,11-trimethyl-2,6,10-dodecatrienol', '3,7,11-trimethyl-2,6,10-dodecatrien-1-ol',
                        'trimethyl dodecatrienol'],
    "linalool": ['hydroperoxides of linalool', 'linalool']
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check_ingredients():
    selected_list_name = request.form.get("dropdown")
    user_ingredients = request.form.get("user_list")
    ingredients_list = user_ingredients.lower().split(", ")

    unsafe_ingredients = []
    if selected_list_name in predefined_list:
        for ingredient in ingredients_list:
            if ingredient in predefined_list[selected_list_name]:
                unsafe_ingredients.append(ingredient)

    if not unsafe_ingredients:
        message = "Product is safe."
    else:
        message = f"Product is not safe, it contains: {', '.join(unsafe_ingredients)}."

    return render_template('result.html', message=message)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host="localhost")
