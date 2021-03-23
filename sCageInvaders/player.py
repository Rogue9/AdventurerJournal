from turtle import Turtle
from bullet import Bullet

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.hideturtle()
        self.shape('cagebottom.gif')
        self.penup()
        self.goto(0, -350)
        self.showturtle()

    def right(self):
        self.forward(2)

    def left(self):
        self.back(2)

    def fire(self):
        bx = self.xcor()
        by = self.ycor()
        bullet.penup()
        bullet.goto(bx, by + 1)
        bullet.showturtle()
        while 1==1:
            bullet.move()