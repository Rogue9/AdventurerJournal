from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__(shape='circle')
        self.color('white')
        self.setheading(random.randint(0, 359))
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def roll(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_hit(self):
        self.x_move *= -1
        self.move_speed *=0.9


    def new_ball(self, direction):
        self.goto(0,0)
        self.move_speed = 0.1
        if direction == "left":
            self.x_move = -10
        if direction == "right":
            self.x_move = 10

    # def speed_up(self):
    #     self.x_move+=5
    #     self.y_move+=5



