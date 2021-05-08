import turtle

initial_coordinates = [0, -20, -40]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for turtle_index in range(0, 3):
            new_turtle = turtle.Turtle(shape='square')
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=initial_coordinates[turtle_index], y=0)
            self.segments.append(new_turtle)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(x=self.segments[segment - 1].xcor(), y=self.segments[segment - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)