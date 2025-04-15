from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from walls import Walls
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=1200, width=1200)
screen.title("Pong")
screen.bgcolor("black")

right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)
ball = Ball()
scoreboard = Scoreboard()
wall = Walls()


screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    # Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
    # No collision with right paddle
    if ball.xcor() > 360:
        ball.change_direction()
        scoreboard.left_score()
    # No collision with left paddle
    if ball.xcor() < -360:
        ball.change_direction()
        scoreboard.right_score()
screen.exitonclick()
