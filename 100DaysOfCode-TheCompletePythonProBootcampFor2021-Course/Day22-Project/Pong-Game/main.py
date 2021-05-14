import turtle
import paddle

INITIAL_POSITION_RIGHT = [350, 0]
INITIAL_POSITION_LEFT = [-350, 0]

# Create a screen objet from turtle module
screen = turtle.Screen()

# Setting up screen elements
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

right_paddle = paddle.Paddle(INITIAL_POSITION_RIGHT[0], INITIAL_POSITION_RIGHT[1])
left_paddle = paddle.Paddle(INITIAL_POSITION_LEFT[0], INITIAL_POSITION_LEFT[1])

# Setting up a screen listener
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")



# Only close the screen when click a button
screen.exitonclick()