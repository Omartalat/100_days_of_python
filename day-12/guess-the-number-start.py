#!/usr/bin/env python3
"""
Number Guessing Game Objectives:
 Include an ASCII art logo.
 Allow the player to submit a guess for a number between 1 and 100.
 Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
 Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
 If they got the answer correct, show the actual answer to the player.
 Track the number of turns remaining.
 If they run out of turns, provide feedback to the player. 
"""
from art import logo
from random import randint


#  Include an ASCII art logo.
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")
#  Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty.")
    exit()
#  Allow the player to submit a guess for a number between 1 and 100.
guess_number = int(input("Make a guess: "))
if guess_number > 100 or guess_number < 1:
    print("Invalid number.")
    exit()
random_number = randint(1, 100)
#  Track the number of turns remaining.
for _ in range(attempts):
    attempts -= 1
    #  If they run out of turns, provide feedback to the player.
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        exit()
    #  Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    elif guess_number > random_number:
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
    elif guess_number < random_number:
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
    #  If they got the answer correct, show the actual answer to the player.
    else:
        print("You got it! The answer was", random_number)
        exit()
