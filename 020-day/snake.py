from turtle import Turtle

class Snake:
    """
    Represents a snake object in the game.

    Attributes:
    - segments: A list of turtle segments that make up the snake.
    - head: The head segment of the snake.

    Methods:
    - create_snake(): Creates the initial segments of the snake.
    - move(distance): Moves the snake forward by the specified distance.
    - up(): Changes the snake's direction to up.
    - down(): Changes the snake's direction to down.
    - left(): Changes the snake's direction to left.
    - right(): Changes the snake's direction to right.
    """

    def __init__(self):
        self.segments = self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates the initial segments of the snake.

        Returns:
        - segments: A list of turtle segments that make up the snake.
        """
        segments = []
        x = 0
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            x -= 20
            segment.goto(x=x, y=0)
            segments.append(segment)
        return segments

    def move(self, distance):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
