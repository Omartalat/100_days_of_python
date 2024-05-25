#!/usr/bin/python3
""""""
from turtle import Turtle
DISTANCE = 20


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.draw_dashline()
        self.sety(200)
        self.update_score()

    def update_score(self):
        self.write(f"{self.left_score}    {self.right_score}", False,
                   "center", ("Pong Game", 64, "normal"))
    
    def draw_dashline(self):
        self.penup()
        self.goto(0, -290)
        self.pensize(3)
        for _ in range(15):
            self.pendown()
            self.forward(DISTANCE)
            self.penup()
            self.forward(DISTANCE)

    def increase_right_score(self):
        self.right_score +=1
        self.clear()
        self.draw_dashline()
        self.sety(200)
        self.update_score()

    def increase_left_score(self):
        self.left_score +=1
        self.clear()
        self.draw_dashline()
        self.sety(200)
        self.update_score()

