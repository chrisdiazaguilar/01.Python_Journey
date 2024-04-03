import random
# Line 3 through 5 we create our variables

name = "Chris"
question = "Will I win the lotter?"
answer = ""

# Line 9 we use the built-in random function to pick a number 1 through 12 everytime we run the code

random_number = random.randint(1, 12)


# Line 14 through 39 uses if, elif, else statement to generate different responses

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Ask again later"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "In the seventh moon you will see it"
elif random_number == 11:
  answer = "Almost there"
elif random_number == 12:
  answer = "Get a job bum"
else:
  answer = "Error"

# Instead of using the format method we use concatenate method to print our results

print(name + " " + "asks:" + " " + question)

print("Magic 8-Ball's answer:" + " " + answer)