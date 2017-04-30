from datetime import datetime ## imports

date = datetime.now() # Date valued to current date.

name = input("Please enter your name: ") # Input for your name

print("1. Pizza") # Names of items.
print("2. Spaghetti")
print("3. Salad")

food = int(input("Make your choice ")) # Menu for food.

print("1. Beer") # Entries of drinks
print("2. Coke")
print("3. Ice Tea")

drink = int(input("What drink would you like? "))

if (food == 1):
    food_price = 9.00 # Price of item
    food_name = "Pizza" # Name of item, has to be put here again.
if (food == 2):
    food_price = 8.50
    food_name = "Spaghetti"
if (food == 3):
    food_price = 4.50
    food_name = "Salad"
if (drink == 1):
    drink_price = 3.00
    drink_name = "Beer"
if (drink == 2):
    drink_price = 1.80
    drink_name = "Coke"
if (drink == 3):
    drink_price = 1.60
    drink_name = "Ice Tea"

tax = 0.06 # Tax percentage, divide the percentage by 100.
tax_percent = tax * 100 # Multiplies decimal by 100
food_price = food_price + food_price * tax # Calculates price of food incl. tax
drink_price = drink_price + drink_price * tax # Calculates price of drink incl. tax
total_price = food_price + drink_price # Total price of drink and food.
food_item = food_name + "  " + str("${:.2f}".format(food_price)) # 2f = 2 decimals.
drink_item = drink_name + "  " + str("${:.2f}".format(drink_price))
print("DATE = " + str(date))# Prints date
print("NAME = " + name) # Prints name
print(food_item) # Prints name of food on receipt.
print(drink_item) # Prints name of drink on receipt.
print("TAX = {}%".format(tax_percent)) # Prints tax
print("PRICE = ${:.2f}".format(total_price)) # Prints total price












