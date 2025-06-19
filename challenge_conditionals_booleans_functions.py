# This file includes three exercises that demonstrate how to use conditionals, booleans, and basic functions in Python.
# Topics covered: comparison operators, if-else statements, arithmetic logic, and simple function implementation.

#Q1) You are given two numbers stored in num1 and num2. If the sum of num1 and num2 is NOT equal to 10, then store True into a variable called not_ten, otherwise store False in not_ten.

num1 = 6
num2 = 3

if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False

print("Is the sum of the numbers not equal to 10? " + str(not_ten))

#_________________________

#Q2) You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget! First, store the total of all expenses into a variable called total. Next, check if the total is greater than the budget. If it is, store True into a variable called over_budget, otherwise store False in over_budget.

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget
if total >= budget:
  over_budget = True
else:
  over_budget = False

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))

#_________________________

#Q3) For the next code challenge, let’s add functions to the mix! We create a function that tests whether the result of taking the power of one number to another number provides an answer that is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. 

# Write your large_power function here:
def large_power(base, exponent):
  product = base ** exponent
  if product > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
print(large_power(2, 12))

