import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(x=-230, y=270)
        self.color("black")
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"Game Over", align="center", font=("Courier", 25, "bold"))
