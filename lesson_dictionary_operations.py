# This script explores key dictionary operations in Python, including creation, updating, overwriting, and comprehension.
# It ends with a mini-project that builds a music library using nested dictionaries and dynamic updates.

#Building a dictionary
sensors =  {"pantry": 22, "living room": 21, "kitchen": 23, "bedroom": 20}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(sensors)

#_________________________________________________
#Adding single elements to a dictionary
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

#_________________________________________________
#Adding multiple items to a dictionary at one time
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#_________________________________________________
#Overwriting dictionary values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

#_________________________________________________
#Dictionary Comprehension
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}

#_________________________________________________
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays_zipped = zip(songs, playcounts)
plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)
print('\n')

#Updating dictionary values
plays["Purple Haze"] = 1
plays["Respect"] = 94

#New dictionary creation 
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)











