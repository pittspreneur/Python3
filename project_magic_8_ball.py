# This code acts as a simplified version of the Magic 8 Ball toy.
# It randomly selects an answer to a user’s question using conditional logic and Python’s random module.

import random

name = "Pittspreneur"
question = "Will I get a promotion?"
answer = ""
random_number = random.randint(1, 9)


if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  print("Error")

print(name + " asks: " + str(question) + "\n")
print("Magic 8-Ball's answer: " + answer)





