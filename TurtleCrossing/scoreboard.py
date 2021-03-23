from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def scored(self):
        self.level +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-275, 260)
        self.write(f'LEVEL: {self.level}', align="left", font=(FONT))

    def game_over(self):
        self.goto(0,-10)
        self.write('SPLAT', align='center', font=FONT)