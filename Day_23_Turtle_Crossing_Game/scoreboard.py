from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.display_score()

    def display_score(self):
        self.write(f"Level:{self.score}", align='left', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level:{self.score}", align='left', font=FONT)
