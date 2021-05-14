import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.create_paddle(x_cord, y_cord)

    def create_paddle(self, x_cord, y_cord):
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_cord, y=y_cord)


    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 10)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 10)
