from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# TODO: SET A FIELD OF CARS TO START, and then generate new cars starting off screen. All cars should be moving forward
# at all times
STARTING_CARS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
class CarManager:
    def __init__(self):

        self.cars = []
        self.start_engines()

    def new_car(self):
        car = Turtle(shape='square')
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.shape('square')
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(random.randint(-270, 270), random.randint(-250,250))
        self.cars.append(car)

    def start_engines(self):
        for i in STARTING_CARS:
            self.new_car()

    def move(self):

        for car_num in range(len(self.cars)):
            if self.cars[car_num].xcor() < -300:
                self.cars[car_num].goto(310, random.randint(-250, 280))
            else:
                new_y = self.cars[car_num].ycor()
                new_x = self.cars[car_num].xcor() - MOVE_INCREMENT
                self.cars[car_num].goto(new_x, new_y)

    def new_new_cars(self):
        chance = random.randint(1,10)
        if chance == 7:
            car = Turtle(shape='square')
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shape('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(340, random.randint(-250,250))
            self.cars.append(car)




