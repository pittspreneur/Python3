# This program organizes some of the sales data for Pitts' Pizza by sorting, slicing, counting, and altering lists.
# It tracks pizza prices, builds a 2D list, identifies the cheapest and most expensive items, and modifies the menu.

#Building The Intial List(s)
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
price = [2, 6, 1, 3, 2, 7, 2]

#Gathering Data On Lists
num_two_dollar_slices = toppings.count(2)
num_pizzas = len(toppings)

#Printing String To Check Lists & Data
print("We sell " + str(num_pizzas) + " different kind of pizza!")
print("\n")

#Creating A 2-D List
pizza_and_prices =  [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
print("\n")

#Sorting & Slicing List
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0][1]
pricest_pizza = pizza_and_prices[6][1]

print(pizza_and_prices)
print("\n")
print("The most expensive pizza is " + pricest_pizza + ".")
print("The cheapest pizza is " + cheapest_pizza + ".")
pizza_and_prices
print("\n")

#Removing & Modifying List
pizza_and_prices.pop(6)
pizza_and_prices.insert(3, [2.5, "peppers"])
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)








