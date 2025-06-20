# This program analyzes weekly haircut pricing and sales data for a salon.
# It calculates average prices, total revenue, average daily revenue, and identifies lower-priced styles using list comprehension.

#Given data on haircuts
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Creating total price
total_price = 0 
for price in prices:
  total_price += price

#Finding the average sales price
average_price = total_price / len(prices)
print("Avergae Haircut Price: " + str(average_price))

#New price list comprehension
new_prices = [price - 5 for price in prices]
print(new_prices)

#Calculating Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: $" + str(total_revenue))

average_daily_revenue = total_revenue / 7

#List Compensation
cuts_under_30 = [hairstyles[i] for i in range(len(prices)) if prices[i] < 30]
print(cuts_under_30)

  
  
