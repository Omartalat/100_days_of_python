#!/usr/bin/python3
""""""
from turtle import Turtle
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # shape
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.left(90)
        # pen
        self.penup()
        # position
        self.goto(position)

    def move(self):
        if abs(self.ycor()) < 260:
            self.forward(DISTANCE)
        else:
            self.left(180)
            self.forward(DISTANCE)

    def up(self):
        if self.ycor() < 260:
            self.forward(DISTANCE)

    def down(self):
        if self.ycor() > -260:
            self.backward(DISTANCE)