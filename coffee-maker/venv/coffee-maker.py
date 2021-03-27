from data import resources, MENU


def check_resources():
    print("Checking resources...")

def make_drink(drink):
    print("Making drink...")
    resources['water'] -= drink['water']
    resources['coffee'] -= drink['coffee']
    if drink != 'expresso':
        resources['milk'] -= drink['milk']



drink_order = input("What would you like? \(expresson/latte/cappuccino\): ")
