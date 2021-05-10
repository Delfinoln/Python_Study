import turtle

initial_coordinates = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creating a snake body
    def create_snake(self):
        for turtle_index in range(0, 3):
            new_turtle = turtle.Turtle(shape='square')
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=initial_coordinates[turtle_index], y=0)
            self.segments.append(new_turtle)

    # Moving the snake forward
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(x=self.segments[segment - 1].xcor(), y=self.segments[segment - 1].ycor())
        self.head.forward(MOVE_DISTANCE)


    # Turning methods
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())


    def add_segment(self, position):
        new_turtle = turtle.Turtle(shape='square')
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)