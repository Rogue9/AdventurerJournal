def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

add(7,9,10,5,3,9,23,0,7,5,14,9,3,2)

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']

print(calculate(5, add=4, multiply=3))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)