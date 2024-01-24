"""
Summary:
The purpose of this script is to create an app for a Grocery list.
TODO
1) As a User, I should be continually prompted so that I can add a grocery item or view my list when I need to.
2) As a User, I should be able to ask for HELP so that I can understand how to use the application
3) As a User, I should be able to add an item to the list
4) As a User, upon adding an item to a list, I should known the total length of my list, so that I don't over buy.
5) As a User, I should be able to see the list at anytime so that I can verify my order
6) As a User, I should be able to state when I am DONE, so that I may print out the list in totality
"""

# Create a new empty list named shopping_list

shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'Done' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' for to see your current list.
    """)


# Create a function named add_to_list that declares a parameter named item
# Add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    # Notify user that the item was added, and state the number of items in the list currently
    print("Added! List has {} items.".format(len(shopping_list)))


# Define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    # Enable the SHOW command to show the list. Don't forget to update the HELP documentation.
    # HINT: Make sure to run it.
    elif new_item == 'SHOW':
        show_list()
        continue

    # Call add_to_list with new_item as an argument
    add_to_list(new_item)

show_list()