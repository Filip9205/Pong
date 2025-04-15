from turtle import Turtle

operators = ("-", "+")


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("purple")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def change_direction(self):
        self.goto(x=0, y=0)
        self.x_move *= -1
        self.y_move += -1
        self.ball_speed = 0.1
        self.move()



