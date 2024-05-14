#!/usr/bin/python3
"""
This script generates a Hirst painting using turtle graphics.

The script uses the turtle module to create a colorful grid of dots, resembling a Hirst painting.
The colors for the dots are randomly selected from a predefined color list.
"""

from turtle import Turtle, Screen
import random

color_list = [(250, 246, 243), (248, 245, 246), (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244)]
turtle = Turtle()
turtle.speed(0)
turtle.penup()
turtle.hideturtle()
Screen().colormode(255)

def new_row(distance):
    """
    Move the turtle to a new row.

    Args:
        distance (int): The distance to move the turtle vertically.

    Returns:
        None
    """
    (_, y) = turtle.pos()
    turtle.penup()
    turtle.setpos(0, y + distance)

for _ in range(10):
    for _ in range(10):
        color = random.choice(color_list)
        turtle.dot(20, color)
        turtle.forward(50)
    new_row(50)

screen = Screen()
screen.exitonclick()
