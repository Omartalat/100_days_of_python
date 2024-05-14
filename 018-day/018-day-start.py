#!/usr/bin/python3
"""

"""
from turtle import Turtle, Screen
import random


tim = Turtle()
Screen().colormode(255)

# challenge: drawing a dash

# for _ in range(4):
#     tim.forward(100)
#     tim.penup()
#     tim.backward(25)
#     tim.right(90)
#     tim.backward(25)

# ===========================================

# challenge: drawing a pentagon
# Screen().colormode(255)

# def draw_shape(x):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.color(r, g, b)
#     for _ in range(x):
#         angle = 360 / x
#         tim.right(angle)
#         tim.forward(100)

# for x in range(3, 11):
#     draw_shape(x)

# =========================================

# challenge: random walk
tim.speed("fast")
tim.pensize(15)
angle = [0, 90, 180, 270]

for _ in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)
    tim.forward(30)
    tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()