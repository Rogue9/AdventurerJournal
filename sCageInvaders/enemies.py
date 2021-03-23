from turtle import Turtle

class Enemy1(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.speed('fast')
        self.penup()
        self.shape('cage.gif')
        self.showturtle()



    # def create_line(self):
    #     for position in LINE_1:
    #         self.add_enemy(position)
    #     for position in LINE_3:
    #         self.add_enemy(position)

    def add_enemy(self, coords):
        new_enemy = Turtle(shape='cage.gif')
        new_enemy.penup()
        new_enemy.goto(coords)


    def move(self):
        pass
        # for enemy in self.enemies:
        #     right = self.right.xcor()
        #     left = self.left.xcor()
        #     if right > 500:
        #         self.setheading(180)
        #         self.forward(25)
        #     elif left < -500:
        #         self.setheading(-180)
        #         self.forward(25)



class Enemy2(Turtle):
    def __init__(self):
        super(Enemy2, self).__init__(visible=False)
        self.speed('fast')
        self.penup()
        self.shape('cage2.gif')
        self.showturtle()






    def move(self):
        pass
        # for enemy in self.enemies:
        #     right = self.right.xcor()
        #     left = self.left.xcor()
        #     if right > 500:
        #         enemy.setheading(180)
        #         enemy.forward(25)
        #     elif left < -500:
        #         enemy.setheading(-180)
        #         enemy.forward(25)
