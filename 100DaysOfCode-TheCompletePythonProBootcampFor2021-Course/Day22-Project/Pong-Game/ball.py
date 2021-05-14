import turtle
import random


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.y_pace = 10 * random.choice([1, -1])
        self.x_pace = 10 * random.choice([1, -1])
        self.create_ball()
        self.pace = 0.05

    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed(1)
        self.penup()

    def move(self, l_paddle, r_paddle, scoreboard):
        self.detect_collision(l_paddle, r_paddle)
        self.detect_goal(scoreboard)
        self.goto(x=self.xcor() + self.x_pace, y=self.ycor() + self.y_pace)

    def detect_collision(self, l_paddle, r_paddle):
        # Detect collision with the wall
        if 300 - abs(self.ycor()) < 20:
            self.y_pace *= (-1)

        # Detect collision with a paddle
        if (self.distance(r_paddle) < 50 and self.xcor() > 320) or (
                self.distance(l_paddle) < 50 and self.xcor() < -320):
            self.x_pace *= (-1)
            self.pace *= 0.9

    def detect_goal(self, scoreboard):
        if self.xcor() > 380:
            self.goto(x=0, y=0)
            self.x_pace *= (-1)
            self.pace = 0.05
            scoreboard.l_score += 1
            scoreboard.write_new_score()

        elif self.xcor() < -380:
            self.goto(x=0, y=0)
            self.x_pace *= (-1)
            self.pace = 0.05
            scoreboard.r_score += 1
            scoreboard.write_new_score()
