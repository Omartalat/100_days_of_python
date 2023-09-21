#!/usr/bin/env python3
"""
Blackjack game.
############### Our Blackjack House Rules #####################
1. The deck is unlimited in size. 
2. There are no jokers. 
3. The Jack/Queen/King all count as 10.
4. The the Ace can count as 11 or 1.
5. Use the following list as the deck of cards:
6. cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
7. The cards in the list have equal probability of being drawn.
8. Cards are not removed from the deck as they are drawn.
9. The computer is the dealer.
"""
import os
from art import logo
from random import choice

def clear_terminal():
    """
    clear terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(user_score, computer_score):
  """
  compare user score and computer score
  """
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

deck = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11 ]

player_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while player_answer == "y":
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    player_continue = "y"
    print(logo)
    for i in range(2):
        player_hand.append(choice(deck))
        dealer_hand.append(choice(deck))
    player_score= sum(player_hand)
    dealer_score = sum(dealer_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {player_hand[0]}")
    player_continue =input("Type 'y' to get another card, type 'n' to pass: ")
    while player_continue == "y":
        player_hand.append(choice(deck))
        player_score = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {player_hand[0]}")
        player_continue =input("Type 'y' to get another card, type 'n' to pass: ")
    print(compare(player_score, dealer_score))
    player_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear_terminal()