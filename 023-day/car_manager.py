#!/usr/bin/python3
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    A class that represents a car manager.

    Attributes:
        car_speed (int): The speed of the cars.
        speed_increment (int): The amount by which the car speed increases.
        cars (list): A list of car objects.

    Methods:
        create_cars(): Creates new car objects.
        move(): Moves the cars forward.
        increase_speed(): Increases the speed of the cars.
    """

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.speed_increment = MOVE_INCREMENT
        self.cars = []

    def create_cars(self):
        """
        Creates new car objects.

        The number of cars created is determined randomly.
        The shape, color, and position of each car are also randomly determined.
        """
        randnum = random.randint(1, 4)
        if randnum == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            y = random.randrange(260, -250, -30)
            car.goto(x=300, y=y)
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        """
        Moves the cars forward.

        Each car in the list of cars moves forward by the car speed.
        """
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        """
        Increases the speed of the cars.

        The car speed is increased by the speed increment.
        """
        self.car_speed += self.speed_increment
