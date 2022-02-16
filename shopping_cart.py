# shopping_cart.py

import datetime
from more_itertools import product_index


products = [
    {
        "id": 1,
        "name": "Chocolate Sandwich Cookies",
        "department": "snacks",
        "aisle": "cookies cakes",
        "price": 3.50
    },


    {"id": 2, "name": "All-Seasons Salt", "department": "pantry",
        "aisle": "spices seasonings", "price": 4.99},
    {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea",
        "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce",
        "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry",
        "aisle": "marinades meat preparation", "price": 7.99},
    {"id": 6, "name": "Dry Nose Oil", "department": "personal care",
        "aisle": "cold flu allergy", "price": 21.99},
    {"id": 7, "name": "Pure Coconut Water With Orange",
        "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash",
        "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id": 9, "name": "Light Strawberry Blueberry Yogurt",
        "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage",
        "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id": 11, "name": "Peach Mango Juice", "department": "beverages",
        "aisle": "refrigerated", "price": 1.99},
    {"id": 12, "name": "Chocolate Fudge Layer Cake",
        "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id": 13, "name": "Saline Nasal Mist", "department": "personal care",
        "aisle": "cold flu allergy", "price": 16.00},
    {"id": 14, "name": "Fresh Scent Dishwasher Cleaner",
        "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id": 15, "name": "Overnight Diapers Size 6",
        "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id": 16, "name": "Mint Chocolate Flavored Syrup",
        "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood",
        "aisle": "poultry counter", "price": 9.99},
    {"id": 18, "name": "Pizza for One Suprema Frozen Pizza",
        "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend",
        "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink",
        "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71


######################
# start of main code #
######################

# VARIABLE DECLARATIONS
total_price = 0 # initialize counter variable
selected_ids = [] # store user inputted IDs into a list
product_ids = []  # used for data validation; store all product ids into a list
for item in products:
    product_ids.append(item["id"])

# ASK FOR USER INPUT AND STORE INTO LIST IF VALID
while True:
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if selected_id == "DONE":
        break
    elif str(selected_id) not in str(product_ids):
        print("Error, you have entered an invalid ID. Please try again.")
    else:
        selected_ids.append(selected_id)

# RECEIPT OUTPUT HEADER
print("---------------------------------")
print("LESLEY'S LOCAL GROCERY")
print("WWW.LESLEYSGROCERY.COM")
print("---------------------------------")

# print current date and time
print("CHECKOUT AT:", datetime.datetime.now())  # NEED TO REFORMAT TIME
print("---------------------------------")

# FIND MATCHING PRODUCTS AND PRICES; RUNNING SUM OF TOTAL
print("SELECTED PRODUCTS:")
for selected_id in selected_ids:
    matching_products = []
    for p in products:
        if str(p["id"]) == str(selected_id):
            matching_products.append(p)
    matching_product = matching_products[-1]
    total_price = total_price + matching_product["price"]
    print("... " + matching_product["name"] + " (" + str(to_usd(matching_product["price"])) + ")")

# PRINT TOTALS
print("---------------------------------")
print("SUBTOTAL: ", to_usd(total_price))

# determine tax rate and final total
tax_rate = .0875
tax_owed = total_price * tax_rate
print("TAX:", to_usd(tax_owed))
print("TOTAL:", to_usd(total_price + tax_owed))

# farewell message
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
