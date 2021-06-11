import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = []

for i in range(240, -240, -20):
    POSITIONS.append(i)


class CarManager(Turtle):

    def __init__(self,):
        super().__init__()
        self.all_cars = []
        self.speed = 3
        self.create_cars()

    def create_cars(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.resizemode("user")
        self.shapesize(1, 2, 1)
        self.penup()
        self.setheading(180)
        self.position_cars()
        self.all_cars.append(self)

    def position_cars(self):
        x_cor = random.choice(POSITIONS)
        y_cor = random.choice(POSITIONS)
        self.goto(x_cor, y_cor)

    def refresh_position(self):
        y_cor = random.choice(POSITIONS)
        self.goto(290, y_cor)

    def move(self):
        for _ in self.all_cars:
            self.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
