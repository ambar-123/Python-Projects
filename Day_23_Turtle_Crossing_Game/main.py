import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross The Turtle")
screen.tracer(0)

screen.listen()

turtle = Player()
screen.onkeypress(turtle.move_up, "Up")

cars = [CarManager() for _ in range(20)]

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car = random.choice(cars)
    car.move()
    if car.xcor() < -280:
        car.refresh_position()
        car.move()

    if turtle.ycor() > 280:
        turtle.start_location()
        scoreboard.increase_score()
        car.increase_speed()

    for car in cars:
        if turtle.distance(car) < 22:
            game_is_on = False
            turtle.penup()
            turtle.goto(0,0)
            turtle.write(f"GAME OVER", align='center', font=("Courier", 20, "bold"))

screen.exitonclick()
