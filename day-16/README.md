# Coffee Machine Simulation

## Overview

This Python program simulates a coffee machine that can take orders, check resources, accept payment, and make coffee. It provides a user-friendly interface for interacting with the coffee machine, allowing users to place orders for various coffee drinks from a menu, check the status of available resources, and turn off the machine.

The program is organized into several modules:
- `menu.py`: Contains the `Menu` class, which defines the menu of available coffee drinks and their respective prices.
- `coffee_maker.py`: Contains the `CoffeeMaker` class, responsible for managing the coffee machine's resources and making coffee.
- `money_machine.py`: Contains the `MoneyMachine` class, responsible for handling payments.

## How to Use

To use the coffee machine simulation program, follow these instructions:

1. Clone or download the program repository to your local machine.

2. Ensure you have Python 3 installed on your system.

3. Open a terminal or command prompt and navigate to the program directory.

4. Run the program by executing the following command:

   ```
   python3 coffee_machine.py
   ```

5. Once the program is running, you can interact with the coffee machine by following the prompts.

   - To place an order, type the name of a coffee drink from the menu and press Enter.
   - To check the status of available resources, type "report" and press Enter.
   - To turn off the coffee machine, type "off" and press Enter.

6. If you place an order, the program will check if there are enough resources to make the selected drink. If resources are sufficient, you will be prompted to make a payment.

7. To make a payment, follow the instructions provided by the Money Machine. If the payment is successful, the coffee machine will prepare your drink.

8. You can continue placing orders, checking resources, or turning off the machine as needed.

## Example Usage

Here's an example of how to use the program:

```
What would you like? (latte/espresso/cappuccino): latte
Please insert coins.
How many quarters?: 2
How many dimes?: 0
How many nickels?: 1
How many pennies?: 0
Here is $2.25 in change.
Here is your latte. Enjoy!

What would you like? (latte/espresso/cappuccino): report
Water: 500ml
Milk: 450ml
Coffee: 50g
Money: $2.25

What would you like? (latte/espresso/cappuccino): off
```

## License

This program is provided under the MIT License. You can find the full license text in the `LICENSE` file.

## Author

@Omartalat

If you have any questions or feedback, please feel free to contact me at dr.omartalat@gmail.com.

