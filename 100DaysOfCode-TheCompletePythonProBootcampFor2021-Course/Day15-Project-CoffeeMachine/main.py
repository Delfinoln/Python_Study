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
    "money": 2.5,
}


def check_resources(drink):
    for resource in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][resource] > resources[resource]:
            print(f'Sorry there is not enough {resource}')
            return False
        else:
            return True


def process_coins():
    print('Please insert coins')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    total_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

    return total_money


mode_off = False
action = ''

while not mode_off:
    action = input('What would you like? (espresso/latte/cappuccino): ')

    if action == 'off':
        mode_off = True
    elif action == 'report':
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')
    elif action == 'espresso' or action == 'latte' or action == 'cappuccino':
        if check_resources(action):
            total_paid = process_coins()
            if total_paid < MENU[action]['cost']:
                print("Sorry that's not enough money. Money refunded")
            else:
                change = total_paid - MENU[action]['cost']
                resources['money'] += MENU[action]['cost']
                for ingredient in MENU[action]['ingredients']:
                    resources[ingredient] -= MENU[action]['ingredients'][ingredient]

                print(f'Here is ${change} in change.\nHere is your {action}')









