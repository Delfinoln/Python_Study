import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)

    def show_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))


    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))
