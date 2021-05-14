import turtle


class Character(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def move_down(self):
        if self.ycor() > -280:
            self.backward(20)