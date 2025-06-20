# This script uses list comprehension and Python's random module to generate a list of random integers.
# It then selects and prints one random element from the list using random.choice().


import random

random_list = []
random_list = [random.randint(1, 100) for i in range(101)]

randomer_number = random.choice(random_list)

print(randomer_number)
