#!/usr/bin/env python3
"""
This is a simple higher-lower game where the user is presented with two random items
and must guess which one has a higher value. The game keeps track of the user's score
and displays it at the end of each round. The user can choose to continue playing or
quit at any time.
"""

import os
from random import choice

import art
import game_data


def starter(first_data, second_data):
    """
    Takes two dictionaries containing information about two celebrities,
    presents the user with their names, descriptions, and countries,
    prompts the user to guess which celebrity has more followers on Instagram,
    and returns the user's choice as a string.
    """
    print(art.logo)
    print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}")
    print(art.vs)
    print(f"Against B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return player_choice


def compare(first_data, second_data, player_choice):
    """
    The `compare` function takes the two dictionaries,
    the user's choice, and compares the follower count of the two celebrities.
    It returns a boolean value indicating whether the user's choice was correct or not.
    """
    if first_data['follower_count'] > second_data['follower_count']:
        higher_choice = 'A'
        if player_choice == higher_choice:
            return True
        else:
            return False
    if first_data['follower_count'] < second_data['follower_count']:
        higher_choice = 'B'
        if player_choice == higher_choice:
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
    Simulation of the game
    """
    score = 0
    to_continue = True
    first_data = choice(game_data.data)
    second_data = choice(game_data.data)
    while to_continue:
        first_data = second_data
        second_data = choice(game_data.data)
        if first_data == second_data:
            second_data = choice(game_data.data)
        player_choice = starter(first_data, second_data)
        clear()
        print(art.logo)
        to_continue = compare(first_data, second_data, player_choice)
        if to_continue:
            score += 1
            print(f"You're right! Current score: {score}.")
    print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == '__main__':
    game()