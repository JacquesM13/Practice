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
    # "water": 300,
    "water": 100,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

on = True

def report():
    for item, amount in resources.items():
        if item == 'milk' or item == 'water':
            print(f"{item.title()}: {amount}ml")
        elif item == 'coffee':
            print(f"{item.title()}: {amount}g")
        elif item == 'money':
            print(f"{item.title()}: ${amount}")

def money_sort():
    total_coin_value = 0
    print(f"Please enter coins amounting to ${MENU[order]['cost']:.2f} \n")
    total_coin_value += int(input("How many quarters? ")) * 0.25
    total_coin_value += int(input("How many dimes? ")) * 0.10
    total_coin_value += int(input("How many nickels? ")) * 0.05
    total_coin_value += int(input("How many pennies? ")) * 0.01
    print(f"You provided: ${total_coin_value:.2f}")
    return total_coin_value

def resource_update():
    for ingredient, quantity in MENU[order]['ingredients'].items():
        resources[ingredient] -= MENU[order]['ingredients'][ingredient]

def change_calc(cost, money_given):
    change = money_given - cost
    print(f"Your change is ${change:.2f}")

while on:
    insufficient_resources = False
    insufficient_funds = False
    order = input("What would you like? (espresso / latte / cappuccino): ")
    if order == 'off':
        on = False
    elif order == 'report':
        report()
    elif order == 'cappuccino' or order == 'espresso' or order == 'latte':
        for ingredient, quantity in MENU[order]['ingredients'].items():
            if quantity > resources[ingredient]:
                print(f"Insufficient {ingredient}")
                insufficient_resources = True
        if not insufficient_resources:
            total_coins_inserted = money_sort()
            if MENU[order]['cost'] > total_coins_inserted:
                print("You have provided insufficient funds, money refunded")
                insufficient_funds = True
            if not insufficient_funds:
                resource_update()
                print(f"The cost of a {order} is: ${MENU[order]['cost']:.2f}")
                if MENU[order]['cost'] < total_coins_inserted:
                    change_calc(MENU[order]['cost'], total_coins_inserted)
                resources['money'] += MENU[order]['cost']
                print(f"Here is your {order}, enjoy!")