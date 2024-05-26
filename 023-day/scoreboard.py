#!/usr/bin/python3
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    A class representing the scoreboard in the game.

    Attributes:
    - level (int): The current level of the game.

    Methods:
    - __init__(): Initializes the Scoreboard object.
    - update_score(): Updates the score on the scoreboard.
    - increase_level(): Increases the level by 1 and updates the score.
    - gameover(): Displays the "GAME OVER" message on the scoreboard.
    """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 250)
        self.update_score()

    def update_score(self):
        """
        Updates the score on the scoreboard.
        """
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def increase_level(self):
        """
        Increases the level by 1 and updates the score.
        """
        self.level += 1
        self.update_score()

    def gameover(self):
        """
        Displays the "GAME OVER" message on the scoreboard.
        """
        self.home()
        self.write("GAME\nOVER", False, "center", FONT)
