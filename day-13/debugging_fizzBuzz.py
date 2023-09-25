#!/usr/bin/env python3


for number in range(1, 101):
  # if number % 3 == 0 or number % 5 == 0:
  # it should check if the number is divisible by 3 and 5 first
  # SOLUTION: if number % 3 == 0 and number % 5 == 0:
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # if number % 5 == 0:
  elif number % 3 == 0:
    print("Fizz")
  # if number % 3 == 0:
  elif number % 5 == 0:
    print("Buzz")
  else:
    #print([number])
    print(number)