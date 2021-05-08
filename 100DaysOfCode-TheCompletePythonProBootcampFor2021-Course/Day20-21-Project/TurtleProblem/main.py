import turtle
import time
import snake

# Creating a Screen object called screen
screen = turtle.Screen()

# Setting up screen elements
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating a snake object
snake = snake.Snake()

# Creating a screen listener to trigger movement function
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Creating movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()


# This method will prevent the screen to close automatically
screen.exitonclick()

