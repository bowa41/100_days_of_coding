from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-200, 260)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT)

    def score_point(self):
        self.score += 1
        self.print_score()


