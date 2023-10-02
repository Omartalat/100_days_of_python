#!/usr/bin/env python3
"""
This program simulates a coffee machine that can take orders, check resources, accept payment, and make coffee. 
It imports the Menu, MenuItem, CoffeeMaker, and MoneyMachine classes from their respective modules. 
The program prompts the user for input, and accepts "off" to exit the program, "report" to print a report of all resources, 
and any item in the menu to place an order. The program then checks if there are enough resources to make the order, 
and if there is, it accepts payment and makes the coffee. 
"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def prompt():
    """Prompt user for input"""
    menu = Menu()
    return input(f"What would you like? ({menu.get_items()}): ").lower()


def exit(prompt):
    """Exit the program"""
    if prompt == "off":
        quit()


def report(prompt, coffee_maker, money_machine):
    """Prints a report of all resources"""
    if prompt == "report":
        coffee_maker.report()
        money_machine.report()


def find_drink(prompt):
    """Finds the drink in the menu"""
    drink = Menu().find_drink(prompt)
    return drink


def check_resources(drink, coffee_maker):
    """Returns True when order can be made, False if ingredients are insufficient."""
    if coffee_maker.is_resource_sufficient(drink):
        return True
    else:
        return False


def check_money(drink, coffee_maker, money_machine):
    """Returns True when payment is accepted, False if payment is insufficient."""
    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
        return coffee_maker, money_machine


def main():
    """Main program"""
    coffeemaker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        order = prompt()
        if order == "off":
            exit(order)
        elif order == "report":
            report(order, coffeemaker, money_machine)
        elif order in Menu().get_items():
            drink = find_drink(order)
            to_continue = check_resources(drink, coffeemaker)
            if to_continue:
                coffeemaker, money_machine = check_money(
                    drink, coffeemaker, money_machine
                )


if __name__ == "__main__":
    main()
