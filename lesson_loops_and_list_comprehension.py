# This program uses for loops to iterate through a list of digits, appends numbers using the append method, and uses list comprehension.
# Demonstrates the creation of squared and cubed lists using both traditional loops and Pythonic list comprehension.

#Building lists
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

#For loop
for digits in single_digits:
  print(digits)
  squares.append(digits**2)
  print(squares)
  
cubes = [digit**3 for digit in single_digits]
print(cubes)
