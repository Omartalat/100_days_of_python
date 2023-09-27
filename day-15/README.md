# Coffee Machine Simulation

The Coffee Machine Simulation is a Python program that simulates the operation of a coffee machine. It allows users to select from a menu of coffee options, check available resources, insert coins, and receive coffee based on their choices.

## Features

- **Menu:** The program offers a menu of coffee options, each with its list of required ingredients and cost.
- **Resources:** The coffee machine has limited resources, including water, milk, and coffee beans.
- **Payment:** Users can insert coins (quarters, dimes, nickels, and pennies) to pay for their chosen coffee.
- **Change:** If users insert more money than the cost of the coffee, the machine calculates and returns the change.
- **Reports:** Users can request a report that displays the current status of resources and money earned.
- **Turn Off:** The machine can be turned off by entering a special "off" command.

## How to Use

1. Run the program by executing the `coffee_machine.py` script using Python 3.

   ```shell
   python3 coffee_machine.py
   ```

2. The program will display a prompt: "What would you like? (espresso/latte/cappuccino):"

3. Follow the prompts and enter one of the following commands:

   - To order a coffee, type the name of the coffee (e.g., "espresso," "latte," "cappuccino").
   - To turn off the machine, type "off."
   - To generate a report, type "report."

4. If you choose to order coffee, the program will guide you through inserting coins. Enter the number of quarters, dimes, nickels, and pennies you want to insert.

5. The program will check if there are enough resources and if you've inserted enough money. If the transaction is successful, it will dispense the coffee and return change if necessary.

6. You can continue to order more coffee, generate reports, or turn off the machine as needed.

## Example Usage

Here's an example of how to use the coffee machine:

1. Run the program and select "latte."
2. Insert coins as prompted.
3. If you've inserted enough money and resources are available, you'll receive your latte.
4. You can check the report to see the updated resource levels and earnings.
5. Continue ordering more coffee or turn off the machine when finished.

## Author

This coffee machine simulation was created by @Omartalat.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
