from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Serif", 28, "bold")


class Score(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(pos, 250)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
