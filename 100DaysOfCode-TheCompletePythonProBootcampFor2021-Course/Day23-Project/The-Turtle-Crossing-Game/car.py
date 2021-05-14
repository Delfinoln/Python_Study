import turtle
import random

COLORS = ["yellow", "green", "blue", "purple", "red", "orange"]

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(300, random.randint(-260, 280))