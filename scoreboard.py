from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=310)
        self.left_player = 0
        self.right_player = 0
        self.score()

    def score(self):
        self.write(f"Player 1: {self.left_player}  Player 2: {self.right_player}", font=("Arial", 20, "bold"),
                   align="center")

    def right_score(self):
        self.right_player += 1
        self.clear()
        self.score()

    def left_score(self):
        self.left_player += 1
        self.clear()
        self.score()
