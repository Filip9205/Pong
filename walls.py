import turtle
from turtle import Turtle


class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.pensize(3)
        self.goto(x=-400, y=300)
        self.draw()

    def draw(self):
        self.pendown()
        for _ in range(2):
            self.forward(800)
            self.right(90)
            self.forward(600)
            self.right(90)

