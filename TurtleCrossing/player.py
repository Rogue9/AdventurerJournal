from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(MOVE_DISTANCE)

    def move_right(self):
        x = self.xcor() + MOVE_DISTANCE
        y = self.ycor()
        if x >= 290:
            self.goto(-290, y)
        else:
            self.goto(x, y)

    def move_left(self):
        x = self.xcor() - MOVE_DISTANCE
        y = self.ycor()
        if x <= -290:
            self.goto(290, y)
        else:
            self.goto(x, y)

    def crossed(self):
        x = self.xcor()
        y = -280
        self.setposition(x, y)
