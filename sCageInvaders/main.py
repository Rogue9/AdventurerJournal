from turtle import Turtle, Screen
import time


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


class Bullet(Turtle):

    def __init__(self):
        super(Bullet, self).__init__()

        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.speed(0)
        self.shape('arrow')
        self.color('chartreuse')

    # def is_collision(self):
    #     if enemies.distance(bullet) < 10:
    #         return True
    #     else:
    #         return False

    def move(self):
        self.forward(20)


class Enemy1():
    def __init__(self):

        enemies2 = []

        self.new_enemy()

    def new_enemy(self):
        enemy = Turtle()
        self.speed('fast')
        self.penup()
        self.shape('cage.gif')
        self.showturtle()
        enemies.append(enemy)



class Enemy2():
    def __init__(self):


        self.new_enemy()

    def new_enemy(self):
        enemy = Turtle()
        self.speed('fast')
        self.penup()
        self.shape('cage2.gif')
        self.showturtle()
        enemies.append(enemy)


LINE_1 = [(200, 375), (100, 375), (0, 375), (-100, 375), (-200, 375), (250, 300), (150, 300), (50, 300), (-50, 300),
          (-150, 300), (200, 225), (100, 225), (0, 225), (-100, 225), (-200, 225), (250, 150), (150, 150), (50, 150),
          (-50, 150), (-150, 150)]

enemies = []

other_enemies = []
is_game_on = True

screen = Screen()
screen.listen()
screen.register_shape('cage.gif')
screen.register_shape('cage2.gif')
screen.register_shape('bullet.gif')
screen.register_shape('cagebottom.gif')
screen.tracer(0)
bullet = Bullet()
bullet.goto(0, -400)
cage = Player()
for i in range(10):
    Enemy1()
for t in range(10, 20):
    Enemy2()

# enemy2 = Enemy2()
for b in range(len(enemies)):
    enemies[b].setposition(LINE_1[b])
print(enemies)
screen.onkeypress(cage.right, 'Right')
screen.onkeypress(cage.left, 'Left')
screen.onkey(cage.fire, 'Up')
while 1 == 1:

    for n in enemies:

        x = enemies[n].xcor()
        y = enemies[n].ycor()
        if enemies[n].xcor() > 400 or enemies[n].xcor() < -400:
            enemies[n].goto(x, y-25)
            if enemies[n].heading() == 0:
                enemies[n].setheading(180)
            else:
                enemies[n].setheading(0)
        enemies[n].forward(20)
        if enemies[n].distance(bullet) < 10:
            enemies[n].goto(-900,-900)
    screen.update()
time.sleep(0.1)
screen.exitonclick()