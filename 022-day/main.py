#!/usr/bin/python3
""""""
import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)

# Create Players
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# Create Scoreboard
scoreboard = Scoreboard()
ball = Ball()

# Movements using keys "Up" & "Down"
# Left Player
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")

# Right Player
not_miss_ball = True
while not_miss_ball:
    right_paddle.move()
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)
    angle = ball.heading()

    # ball bounce when collided with wall
    if abs(ball.ycor()) > 280:
        ball.setheading(360 - angle)

    # ball collision with paddle
    if ball.distance(right_paddle) < 25 or\
       ball.distance(left_paddle) < 25:
        ball.setheading(180 - angle)
        ball.move_speed *= 0.9
    
    # GAMEOVER
    if abs(ball.xcor()) > 395:
        ball.reset_ball()
        if ball.xcor() > 0:
            scoreboard.increase_right_score()
        else:
            scoreboard.increase_left_score()

screen.exitonclick()
