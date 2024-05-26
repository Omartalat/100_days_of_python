#!/usr/bin/python3
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """A class representing the player turtle in the game."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        """Move the player turtle forward."""
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        """Reset the player turtle to the starting position."""
        self.goto(STARTING_POSITION)
