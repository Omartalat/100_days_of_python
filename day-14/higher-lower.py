#!/usr/bin/env python3
"""
This is a simple higher-lower game where the user is presented with two random items
and must guess which one has a higher value. The game keeps track of the user's score
and displays it at the end of each round. The user can choose to continue playing or
quit at any time.
"""
from random import choice
import os
import art
import game_data


def starter(firstData, secondData):
    """
    takes two dictionaries containing information about two celebrities,
    presents the user with their names, descriptions, and countries,
    prompts the user to guess which celebrity has more followers on Instagram,
    and returns the user's choice as a string.
    """
    print(art.logo)
    print(f"Compare A: {firstData['name']}, a {firstData['description']}, from {firstData['country']}")
    print(art.vs)
    print(f"Against B: {secondData['name']}, a {secondData['description']}, from {secondData['country']}")
    playerChoice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return playerChoice

def compare(firstData, secondData, playerChoice):
    """
    The `compare` function takes the two dictionaries, 
    the user's choice, and compares the follower count of the two celebrities. 
    It returns a boolean value indicating whether the user's choice was correct or not.
    """
    if firstData['follower_count'] > secondData['follower_count']:
        higherChoice = 'A'
        if playerChoice == higherChoice:
            return True
        else:
            return False
    if firstData['follower_count'] < secondData['follower_count']:
        higherChoice = 'B'
        if playerChoice == higherChoice:
            return True
        else:
            return False
def clear():
    """
    Clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
def game():
    """
    simulation of the game
    """
    score = 0
    to_continue = True
    firstData = choice(game_data.data)
    secondData = choice(game_data.data)
    while to_continue:
        firstData = secondData
        secondData = choice(game_data.data)
        if firstData == secondData:
            secondData = choice(game_data.data)
        playerChoice = starter(firstData, secondData)
        clear()
        print(art.logo)
        to_continue =  compare(firstData, secondData, playerChoice)
        if to_continue:
            score += 1
            print(f"You're right! Current score: {score}.")
    print(f"Sorry, that's wrong. Final score: {score}")

game()