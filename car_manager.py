from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.start_right()
        self.move()

# make a def for the car to keep going forward
    def move(self):
        self.xcor() += MOVE_INCREMENT
# make a clear definition and to start at the beggining
    def start_right(self):
        self.clear()
        self.goto(x=200,y=random.randint(-260,260))
        self.color(random.choice(COLORS))
