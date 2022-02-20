logo = r"""
   ______      ________             __  ___           __    _          
  / ____/___  / __/ __/__  ___     /  |/  /___ ______/ /_  (_)___  ___ 
 / /   / __ \/ /_/ /_/ _ \/ _ \   / /|_/ / __ `/ ___/ __ \/ / __ \/ _ \
/ /___/ /_/ / __/ __/  __/  __/  / /  / / /_/ / /__/ / / / / / / /  __/
\____/\____/_/ /_/  \___/\___/  /_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/ 
                                                                       
"""
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    for resource in resources:
        prefix = ""
        if resource == "money":
            prefix = "$"
        if resource == "water" or resource == "milk":
            units = "ml"
        elif resource == "coffee":
            units = "g"
        else:
            units = ""
        print(f"{resource}: {prefix}{resources[resource]}{units}")

def ask_for_coins(product):
    money = 0
    while(True):
        print("How many quarters?", end=" ")
        quarters = input()
        print("How many dimes?", end=" ")
        dimes = input()
        print("How many nickles?", end=" ")
        nickles = input()
        print("How many pennies?", end=" ")
        pennies = input()
        money += float(quarters) * 0.25 + float(dimes) * 0.10 + float(nickles) * 0.05 + float(pennies) * 0.01
        print(f"total money = {money}")
        # While coins are not enough, ask for more
        if(MENU[product]["cost"] > money):
            print("Insert more coins")
        else:
            break
    return money

def main():
    print(logo)
    valid_option = False
    option = None
    while(True):
        option = None
        # Loop till you get a valid option
        while (True):
            if option != None:
                print("Select a valid option")
            print("What would you like? (espresso/latte/cappuccino):", end=" ")
            option = input()
            # If report is requested, print report and ask for an option again
            if option == "report":
                print_report()
                option = None
                continue
            else:
                for item in MENU:
                    if option == item:
                        valid_option = True
            if valid_option == True:
                break
        valid_option = False
        # Check if there're enough ingredients to prepare
        enough_ingredients = True
        for ingredient in MENU[option]["ingredients"]:
            # First check if there're enough ingredients to prepare the selected product
            if not resources[ingredient] >= MENU[option]["ingredients"][ingredient]:
                print(f"Sorry, there's not enough {ingredient}")
                enough_ingredients = False
                break
        if enough_ingredients == False:
            continue

        # Ask user to insert coins
        print("Please insert coins")
        money = 0
        money = ask_for_coins(option)
        change = money - MENU[option]["cost"]
        # If there's change, return it
        if change > 0:
            print(f"Here's your change: {change}")
        # Add money to resources
        resources["money"] += money
        # Deduct ingredients needed from out resourses
        for ingredient in MENU[option]["ingredients"]:
            resources[ingredient] -= MENU[option]["ingredients"][ingredient]
        print(f"Enjoy your {option}!")
        option = None

if __name__ == '__main__':
    main()