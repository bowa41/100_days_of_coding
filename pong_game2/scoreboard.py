from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.print_score()

    def score(self,side):
        if side == "left":
            self.lscore += 1
        else:
            self.rscore += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-140, 200)
        self.write(self.lscore, align="center", font=("Courier", 88, "normal"))
        self.goto(140, 200)
        self.write(self.rscore, align="center", font=("Courier", 88, "normal"))