#!/usr/bin/python3
############DEBUGGING#####################


# Describe Problem
def my_function():
  # for i in range(1, 20):
  # range(1, 20) will not include 20
  # SOLUTION: range(1, 21)
  for i in range(1, 21): 
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# randint(1, 6) will include index 6 and not index 0
# SOLUTION: randint(0, 5)
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
# elif year > 1994:
# 1994 will not be included
# SOLUTION: elif year >= 1994:
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?")
# type error: input() returns a string
# SOLUTION: age = int(input("How old are you?"))
age = int(input("How old are you? "))
if age > 18:
# print("You can drive at age {age}.")
# f-string is not used
# SOLUTION: print(f"You can drive at age {age}.")
  print(f"You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# print(pages)
# word_per_page == input("Number of words per page: ")
word_per_page = int(input("Number of words per page: "))
# word_per_page is not assigned to the input
# SOLUTION: word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
# b_list.append(new_item)
# b_list is not indented
# SOLUTION: indented
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])