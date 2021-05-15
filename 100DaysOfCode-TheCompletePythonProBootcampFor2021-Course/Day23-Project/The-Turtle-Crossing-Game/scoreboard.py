import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=280)
        self.write()