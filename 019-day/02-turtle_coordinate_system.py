#!/usr/bin/python3

from turtle import Turtle, Screen
import random


def turtle_race():
    """
    Simulates a turtle race game where the user can bet on the winning turtle.

    The turtles start at the left side of the screen and move forward randomly.
    The first turtle to reach the right side of the screen wins the race.
    The user can enter their bet by providing the color of the turtle they think will win.
    If the user's bet matches the winning turtle's color, they win the game.

    Returns:
        None
    """

    screen = Screen()
    screen.setup(500, 400)
    user_bet = screen.textinput(
        title="Make Your Bet!", prompt="Which turtle will win the race? Enter the color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    width = -200
    turtles = []
    is_race_one = False

    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        width += 60
        new_turtle.goto(x=-240, y=width)
        turtles.append(new_turtle)

    if user_bet:
        is_race_one = True

    while is_race_one:
        for turtle in turtles:
            if turtle.xcor() < 220:
                distance = random.randint(0, 10)
                turtle.forward(distance)
            else:
                is_race_one = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(
                        f"You've guessed correctly! The {winning_color} turtle is the winner!")
                else:
                    print(
                        f"Oops! You've lost. The {winning_color} turtle is the winner 🙃")

    screen.exitonclick()


turtle_race()
