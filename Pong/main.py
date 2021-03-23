from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
import time
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PoNg")
screen.tracer(0)
screen.listen()
right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(left_paddle.go_up, 'w')
screen.onkeypress(left_paddle.go_down, 's')
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.roll()
    screen.update()
    if ball.ycor() > 272 or ball.ycor() < -272:
        ball.bounce()
    # Detect collision with right paddle
    if ball.xcor()> 360 and ball.distance(right_paddle) < 50 or ball.xcor()< -360 and ball.distance(left_paddle) < 50:
        ball.paddle_hit()
    if ball.xcor()> 380:
        ball.new_ball("left")
        score.l_point()
    if ball.xcor()< -380:
        ball.new_ball("right")
        score.r_point()
screen.exitonclick()