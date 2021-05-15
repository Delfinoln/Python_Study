import turtle
import random

COLORS = ["yellow", "green", "blue", "purple", "red", "orange"]

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
        self.cars_list = []
        self.pace = 0.1

    def create_car(self):
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(310, random.randint(-250, 250))

    def move(self):
        for car in self.cars_list:
            car.goto(car.xcor() - 20, car.ycor())
