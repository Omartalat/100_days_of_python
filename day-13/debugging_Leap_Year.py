#!/usr/bin/env python3


# Debugging challenge - Leap Year
# year = input("Which year do you want to check?")
# year is a string, not an integer. So, we need to convert it to an integer.
# year = int(input("Which year do you want to check?"))
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")