# This project simulates a time travel experience by combining modules like datetime, random, and decimal.
# It generates a travel message including the date, time, random future destination, and travel credits.

import datetime as dt
from decimal import Decimal
import custom_module
from random import randint, choice

date = dt.date.today()
time = dt.datetime.now().time()
print("Today's date is " + str(date) + " and the current time is " + str(time) + ".")

Decimal('1000.00')
abs(-5)
Decimal('2.50')

year = randint(2000, 2024)

travel_places = ["Colombia", "Thailand", "Japan"]

choice(travel_places)

def generate_time_travel_message(year, travel_places, decimal):
    print(f"Traveling to {choice(travel_places)} in the year {year} with {decimal} credits!")

decimal = Decimal('1000.00')

generate_time_travel_message(year, travel_places, decimal)
