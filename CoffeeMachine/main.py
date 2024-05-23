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
}

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
total_money_collected = 0
def coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino)")


    # TODO: 3. Print report.
    def report():
        for i in resources:
            if i in ("water", "milk"):
                print(f"Amount of {i} left: {resources[i]}ml")
            else:
                print(f"Amount of {i} left: {resources[i]}g")
        print(f"Money: ${round(total_money_collected,2)}")
        coffee_machine()

    # TODO: 4. Check resources sufficient?
    def check_levels(selection):
        for i in MENU[selection]['ingredients']:
            if MENU[selection]['ingredients'][i] > resources[i]:
                print(f"Sorry there is not enough {i}")
                coffee_machine()
            else:
                return

    def update_resources(selection):
         for i in MENU[selection]['ingredients']:
             resources[i] -= MENU[selection]['ingredients'][i]
             #print(f"Amount of {i} left: {resources[i]}")

    # TODO: 5. Process coins.
    def collect_money():
        print("Please insert coins.")
        quarters = input("how many quarters?: ")
        dimes = input("how many dimes?: ")
        nickels = input("how many nickels?: ")
        pennies = input("how many pennies?: ")
        return (int(quarters) * .25) + (int(dimes) * .1) + (int(nickels) *.05) + (int(pennies) * .01)


    # TODO: 6. Check transaction successful?
    def make_change(drink, money):
        total_cost = float(MENU[drink]['cost'])
        change = round((money - total_cost), 2)
        if money < total_cost:
            print("Sorry that's not enough money.  Money refunded.")
            coffee_machine()
        elif money >= total_cost:
            return change

    # TODO: 7. Make Coffee.
    def brew(selection):
        global total_money_collected
        check_levels(selection)
        money_collected = float(collect_money())
        change = make_change(selection, money_collected)
        total_money_collected += (money_collected - change)
        update_resources(selection)
        print(f"Here is ${change} in change.")
        print(f"Here is your {selection}. Enjoy!")
        coffee_machine()

    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice == "off":
        exit()
    elif user_choice == "report":
        report()
    else:
        brew(user_choice)
coffee_machine()