import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open(r"100DaysOfCode-TheCompletePythonProBootcampFor2021-Course\Day20-21-Project\Snake-Game\data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))


    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"100DaysOfCode-TheCompletePythonProBootcampFor2021-Course\Day20-21-Project\Snake-Game\data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.show_score()


