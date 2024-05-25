import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.penup()
        new_car.shapesize(stretch_len=2)
        random_y = random.randrange(-250, 250, 15)
        new_car.goto(300, random_y)
        self.cars_list.append(new_car)

    def move_cars(self):
        for cars in self.cars_list:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT




