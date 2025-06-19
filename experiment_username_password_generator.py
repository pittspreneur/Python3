# This file contains an early-stage username and password generator concept using string slicing and loops.
# The goal is to generate a username from parts of a name and then build a password based on that username.

def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = []
  for letters in len(user_name):
    password.append(letter)
