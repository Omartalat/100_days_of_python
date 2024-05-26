#!/usr/bin/python3
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Game Objs Creation
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Screen Listen
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 30:
            scoreboard.gameover()
            game_is_on = False

    if player.ycor() > 280:
        player.reset_player()
        scoreboard.increase_level()
        car_manager.increase_speed()


screen.exitonclick()
