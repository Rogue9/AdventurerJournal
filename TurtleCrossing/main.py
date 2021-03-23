import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

sleep_time = 0.1
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgpic("turtlecrossing.gif")
screen.listen()
timmy = Player()
fred = CarManager()
score = Scoreboard()
game_is_on = True
screen.onkeypress(timmy.move_up, 'Up')
screen.onkeypress(timmy.move_down, 'Down')
screen.onkeypress(timmy.move_left, 'Left')
screen.onkeypress(timmy.move_right, 'Right')

while game_is_on:
    fred.move()
    time.sleep(sleep_time)
    screen.update()

    if score.level % 5 == 0:
        fred.new_new_cars()
    for car in fred.cars:
        if car.distance(timmy)< 20:
            timmy.shape('circle')
            timmy.color('crimson')
            timmy.shapesize(stretch_len=2, stretch_wid=2)
            screen.update()
            game_is_on=False
            score.game_over()

    if timmy.ycor() > 290:
        timmy.crossed()
        score.scored()
        score.update_scoreboard()
        sleep_time *= 0.9

screen.exitonclick()
