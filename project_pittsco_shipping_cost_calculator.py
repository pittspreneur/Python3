# Pitts' Shipping Co Program takes the weight of a package and determines the cheapest way to ship that package.
# It compares the cost of standard ground, premium ground, and drone shipping using conditional logic and arithmetic.

#Toggle Weight Here
weight = 4.8

#Ground Shipping
ground_cost = 0
if weight <= 2:
  ground_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  ground_cost = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  ground_cost = weight * 4.00 + 20
else:
  ground_cost = weight * 4.75 + 20

#Premium Ground Shipping
premium_ground_cost = 125.0

#Drone Shipping
drone_cost = 0
if weight <= 2:
  drone_cost = weight * 4.50 
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9.00 
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12.00 
else:
  drone_cost = weight * 14.75 


print(ground_cost)
print(premium_ground_cost)
print(drone_cost)

#Questions
print("The cheapest method to ship a 4.8 pound package would be standard ground shipping at a cost of $34.40.")
print("\n")
print("The cheapest method to ship a 41.5 pound package would be premium ground shipping at a cost of $125.00.")


 
