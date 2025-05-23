import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x, y=y)

    def move_up(self):
        if self.ycor() != 240:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        if self.ycor() != -240:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)
