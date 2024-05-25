#!/usr/bin/python3
""""""
import random
from turtle import Turtle
DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # Ball shape
        self.shape("circle")
        self.color("white")
        # Pen
        self.penup()
        # Speed
        self.setheading(random.randint(0, 259))
        self.move_speed = 0.1

    def move(self):
        self.forward(DISTANCE)

    def reset_ball(self):
        self.home()
        self.setheading(random.randint(0, 259))
        self.move_speed = 0.1
        self.move()
