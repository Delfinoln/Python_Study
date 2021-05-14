import turtle
import paddle
import ball
import time
import scoreboard

INITIAL_POSITION_RIGHT = [350, 0]
INITIAL_POSITION_LEFT = [-350, 0]

# Create a screen objet from turtle module
screen = turtle.Screen()

# Setting up screen elements
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Creating a ball object
ball = ball.Ball()

# Creating a scoreboar
scoreboard = scoreboard.Scoreboard()

right_paddle = paddle.Paddle(INITIAL_POSITION_RIGHT[0], INITIAL_POSITION_RIGHT[1])
left_paddle = paddle.Paddle(INITIAL_POSITION_LEFT[0], INITIAL_POSITION_LEFT[1])

# Setting up a screen listener
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move(left_paddle, right_paddle, scoreboard)
    time.sleep(ball.pace)

# Only close the screen when click a button
screen.exitonclick()
