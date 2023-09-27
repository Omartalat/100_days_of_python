#!/usr/bin/env python3
"""
The coffee machine project is a program that simulates a coffee machine.
The program allows the user to select from a menu of coffee options, including espresso,
latte, and cappuccino.
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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def report():
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: {value}ml")
    print(f"Money: ${money}")


def check_resources(resources, ingredient):
    if resources["water"] - ingredient["water"] >= 0:
        if resources["coffee"] - ingredient["coffee"] >= 0:
            if choice != "espresso":
                if resources["milk"] - ingredient["milk"] >= 0:
                    resources["milk"] -= ingredient["milk"]
                    resources["coffee"] -= ingredient["coffee"]
                    resources["water"] -= ingredient["water"]
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            elif choice == "espresso":
                resources["coffee"] -= ingredient["coffee"]
                resources["water"] -= ingredient["water"]
                return True
        else:
            print("Sorry there is not enough coffee.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False


def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_transaction(total, cost, money):
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False, money
    elif total == cost:
        money += cost
        print(f"Here is your {choice}☕. Enjoy!")
        return True, money
    else:
        change = total - cost
        money += cost
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {choice}☕. Enjoy!")
        return True, money


# TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#           a. Check the user’s input to decide what to do next.
#           b. The prompt should show every time action has completed, e.g. once the drink is
#              dispensed. The prompt should show again to serve the next customer.

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    #          a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    #             the machine. Your code should end execution when this happens.

    if choice == "off":
        exit()

    # TODO: 3. Print report.
    #         a. When the user enters “report” to the prompt, a report should be generated that shows
    #            the current resource values. e.g.
    #            Water: 100ml
    #            Milk: 50ml
    #            Coffee: 76g
    #            Money: $2.5

    elif choice == "report":
        report()

    # TODO: 4. Check resources sufficient?
    #         a. When the user chooses a drink, the program should check if there are enough
    #            resources to make that drink.
    #         b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    #            not continue to make the drink but print: “Sorry there is not enough water.”
    #         c. The same should happen if another resource is depleted, e.g. milk or coffee.

    else:
        for key, value in MENU.items():
            if choice == key:
                ingredient = MENU[key]["ingredients"]
                cost = MENU[key]["cost"]
                to_continue = check_resources(resources, ingredient)

                # TODO: 5. Process coins.
                #          a. If there are sufficient resources to make the drink selected, then the program should
                #             prompt the user to insert coins.
                #          b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
                #          c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
                #             pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
                if to_continue:
                    total = coins()
                    # TODO: 6. Check transaction successful?
                    #          a. Check that the user has inserted enough money to purchase the drink they selected.
                    #             E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
                    #             program should say “Sorry that's not enough money. Money refunded.”.
                    #          b. But if the user has inserted enough money, then the cost of the drink gets added to the
                    #             machine as the profit and this will be reflected the next time “report” is triggered. E.g.
                    #             Water: 100ml
                    #             Milk: 50ml
                    #             Coffee: 76g
                    #             Money: $2.5
                    #          c. If the user has inserted too much money, the machine should offer change.
                    #             E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
                    valid, money = check_transaction(total, cost, money)
                    if not valid:
                        if choice != "espresso":
                            resources["milk"] += ingredient["milk"]
                            resources["coffee"] += ingredient["coffee"]
                            resources["water"] += ingredient["water"]
                        elif choice == "espresso":
                            resources["coffee"] += ingredient["coffee"]
                            resources["water"] += ingredient["water"]


# TODO: 7. Make Coffee.
#          a. If the transaction is successful and there are enough resources to make the drink the
#             user selected, then the ingredients to make the drink should be deducted from the
#             coffee machine resources.
#             E.g. report before purchasing latte:
#             Water: 300ml
#             Milk: 200ml
#             Coffee: 100g
#             Money: $0
#             Report after purchasing latte:
#             Water: 100ml
#             Milk: 50ml
#             Coffee: 76g
#             Money: $2.5
#          b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#             latte was their choice of drink
