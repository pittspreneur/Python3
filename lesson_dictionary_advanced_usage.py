# This lesson explores a wide range of dictionary operations in Python.
# It includes creating dictionaries, updating and removing key-value pairs, accessing keys and values safely, and using dictionary comprehensions.
# It wraps up with real-world examples like a music library, item inventory system, and statistical reporting.

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


#_________________________________________________
#Accessing Dictionary Keys
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])


#_________________________________________________
#Dealing with invalid dictionary keys
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"]) 


#_________________________________________________
Using get to retrieve a key
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)
print(tc_id)
print(stack_id)


#_________________________________________________
#Deleting a key
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", "0")
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


#_________________________________________________
#Getting all keys from dictionaries
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


#_________________________________________________
#Getting all values from dictionaries
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for num in num_exercises.values():
  total_exercises += num

print(total_exercises)


#_________________________________________________
#Getting all items from dictionaries
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for position, age in pct_women_in_occupation.items():
  print("Women make up " + str(age) + " percent of " + position + "s.")


