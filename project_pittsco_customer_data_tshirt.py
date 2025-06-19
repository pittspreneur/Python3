# This program manages customer data for Pitts' T-Shirt Co by accessing, updating, and modifying single and 2-D lists.
# It simulates customer preferences and shipping updates for a small clothing business.

# Building the first name list
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

#Preferred Sizes List
preferred_size = ["Small", "Large", "Medium"]

#Adding Depak's Size
preferred_size.append("Medium")
print(preferred_size)
print("\n")

#Creating The 2-D list 
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
print("\n")

#Chaini Shipping Change
customer_data[2][2] = False

#Ben Shipping Update
customer_data[1].remove(False)

#Customer Data Update
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

