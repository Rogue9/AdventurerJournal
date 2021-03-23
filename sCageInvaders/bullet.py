from turtle import Turtle

class Bullet(Turtle):

    def __init__(self):
        super(Bullet, self).__init__()
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.speed(0)
        self.shape('arrow')
        self.color('chartreuse')

    def move(self):
        self.forward(20)