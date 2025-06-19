# This project simulates a simple retail checkout system for a furniture store.
# It tracks item descriptions, prices, calculates sales tax, and prints a receipt for a customer.

#Loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

#Settee
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
stylish_settee_price = 180.50

#Lamp
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'
luxurious_lamp_price = 52.15

#Tax
sales_tax = .088

#Customer 1
customer_one_total = 0
customer_one_items = ""

#Customer one's first purchase
customer_one_total += lovely_loveseat_price
customer_one_items += lovely_loveseat_description

#Customer one's second purchase
customer_one_total += luxurious_lamp_price
customer_one_items += luxurious_lamp_description

#Customer one's tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Customer one's receipt
print("Customer One Items: ")
print(customer_one_items)
print('\n')
print("Customer One Total: ")
print(customer_one_total)
