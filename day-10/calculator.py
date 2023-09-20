#The code is a simple calculator program, which takes two numbers and performs the calculation as per the user's input. The program is designed using functions and dictionaries, so that it can be extended to add more operations in future.
#The program starts with a welcome message and asks for first number.
#Then the program asks for the operation to be performed on the first number.
#Then the program asks for the second number.
#Then the program performs the calculation and prints the result.
#Then the program asks the user if he wants to continue with the result as the first number.
#If the user answers yes, then the program continues with the result as the first number, otherwise the program starts again asking for the first number.

#!/usr/bin/env python3
"""
Calculator Project
"""
from art import logo


def add(a, b):
  """
  add two numbers
  """
  return a + b

def substract(a, b):
  """
  substract two number
  """
  return a - b

def multiply(a, b):
  """
  multiply two number
  """
  return a * b

def divide(a, b):
  """
  divide two numbers
  """
  return a / b

operations = {"+" : add, 
              "-" : substract, 
              "*" : multiply,
              "/" : divide,              
             }
def calculator():
    """
    calculator function to calculate two numbers
    """
    print(logo)
    should_continue = True
    a = float(input("What is the first number? "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        b = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(a, b)
        print(f"{a} {operation_symbol} {b} = {answer}")
        continue_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_answer == "y":
            a = answer
        else:
            should_continue = False
            calculator()

calculator()