from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super(Paddle, self).__init__(visible=False)
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)
        self.showturtle()

    def up(self):
            self.forward(20)

    def down(self):
            self.back(20)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)