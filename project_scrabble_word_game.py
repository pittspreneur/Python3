# This project creates a Scrabble-style word game scoring system using dictionaries and functions.
# It calculates word scores, tracks each player's words and total points, and allows new words to be added dynamically.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Using list comprehension to create a dictionary
letters_to_points = {key:value for key,value in zip(letters, points)}

#Adding a new key and element to our dictionary
letters_to_points[" "] = 0

#Function for point calculation
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter.upper(), 0)
  return point_total

#Test for brownie word
#brownie_points = score_word("BROWNIE")
#print(brownie_points)

#Player words dictionary
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#Empty dictionary and function that adds points to the empty dictionary
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

#Adds new words for existing players & creates a new list for new players with their word
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = [word]

#Updates all points up for players#
def update_point_totals():
  for player, words in player_to_words.items():
    points = 0
    for word in words:
      points += score_word(word)
    player_to_points[player] = points

#Adds new players and/or words to the game 
def new_word(name, word):
  play_word(name, word)
  update_point_totals()
  print(player_to_words)
  print(player_to_points)

#Entry for players and words
def new_entry(name, word):
  play_word(name, word)
  update_point_totals()
  print("UPDATED SCORE_______________________________")
  print(player_to_words)
  print(player_to_points)
  print("\n")

#User input for game
new_entry("Pitts", "superman")
new_entry("Pitts", "quebec")
new_entry("Pitts", "outrageous")

