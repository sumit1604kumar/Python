# # Coffee Machine project



# menu = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# # print(menu["espresso"]['cost'])
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
# def report(resources):
#     """To return report of the coffee machine"""
#     water = resources["water"]
#     milk = resources["milk"]
#     coffee = resources["coffee"]
#     return f"Water :{water}ml\nMilk :{milk}ml\nCoffee :{coffee}g"
#
# def coins():
#     '''It will take input number of coin from the user'''
#
#     quarter_coins = int(input("How many quarter?:"))
#     dimes_coins   = int(input("How many dimes?:"))
#     nickles_coins = int(input("How many nickles?:"))
#     pennies_coins = int(input("How many pennies?:"))
#
#     quarter_amount = float(0.25 * quarter_coins)
#     dimes_amount   = float(0.10 * dimes_coins)
#     nickles_amount = float(0.05 * nickles_coins)
#     pennies_amount = float(0.01 * pennies_coins)
#
#     return quarter_amount,dimes_amount,nickles_amount,pennies_amount
#
# def choice(guess):
#     if guess == "espresso":
#         amount_espresso = float(menu["espresso"]['cost'])
#         return amount_espresso
#     elif guess == "latte":
#         amount_latte = float(menu["latte"]['cost'])
#         return amount_latte
#     elif guess == "cappuccino":
#         amount_cappuccino = float(menu["cappuccino"]['cost'])
#         return  amount_cappuccino
#
# def resource_left(guess):
#     if guess == "espresso":
#
#         water_amount = resources["water"] - 50
#         coffee_amount = resources["coffee"] -15
#         resources["water"] = water_amount
#         resources["coffee"] = coffee_amount
#
#
#     elif guess == "latte":
#
#         water_amount = resources["water"] - 200
#         coffee_amount = resources["coffee"] - 24
#         milk_amount = resources["milk"] - 150
#         resources["water"] = water_amount
#         resources["coffee"] = coffee_amount
#         resources["milk"] = milk_amount
#
#
#     elif guess == "cappuccino":
#         water_amount = resources["water"] - 250
#         coffee_amount = resources["coffee"] - 24
#         milk_amount = resources["milk"] - 100
#         resources["water"] = water_amount
#         resources["coffee"] = coffee_amount
#         resources["milk"] = milk_amount
#
# def check(guess):
#     water_check = resources["water"]
#     coffee_check = resources["coffee"]
#     milk_check = resources["milk"]
#     if guess == "espresso":
#         if water_check > 50 and coffee_check > 24:
#             return True
#         else:
#             return False
#     if guess == "latte":
#         if water_check > 200 and coffee_check > 24 and milk_check >150:
#             return True
#         else:
#             return False
#     if guess == "cappuccino":
#         if water_check > 250 and coffee_check > 24 and milk_check > 100:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# should_continue = True
#
# total_user_paid = 0
#
# while should_continue == True:
#     user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
#     if user_choice == "report":
#         resource_l = report(resources)  # function report been called here.
#         print(resource_l)
#
#     elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
#         if total_user_paid == 0:
#             print(" Please insert coins.")
#             money = list(coins())   # values are added into the list
#             print(f"coins added {money}")
#             print(f"total you paid :{sum(money)}")
#             total_user_paid = sum(money)
#         if total_user_paid > choice(user_choice):
#             total_user_paid = total_user_paid - choice(user_choice)
#             print(f"you will get a drink {user_choice} with a refund of {total_user_paid}, enjoy the drink")
#             my_check = check(user_choice)
#             if my_check == False:
#                 print(f'not sufficient resource on the machine, pleas fill Water, milk and Coffee')
#                 should_continue = False
#             else:
#                 a = user_choice
#                 resource_left(a)
#
#
#
#
#         else:
#             should_continue = False
#             print("you don't have enough fund")
#
#
#
#
#
#     elif user_choice == "off":
#         should_continue = False
#         print("Program terminated.")
#


# Avobe is My Try

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    print("Please insert coin.")
    total = int(input("How many quarter?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received -drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit = profit + drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] = resources[item] - order_ingredient[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on == True:

    choice = input("What would you like? (espresso/latte/cappucinno): ")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"money :${profit}")
    else:
        drink = MENU[choice]
        if  is_resource_sufficient(drink['ingredients']) == True:
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']) == True:
                make_coffee(choice, drink["ingredients"])





# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#


