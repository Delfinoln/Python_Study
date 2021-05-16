import turtle
import time
import snake
import food
import scoreboard

# Creating a Screen object called screen
screen = turtle.Screen()

# Setting up screen elements
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating a snake and food object
snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

# Creating a screen listener to trigger movement function
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Creating movement
game_is_on = True
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()
    scoreboard.show_score()

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.score += 1
        snake.extend()

    # Detect collision with the wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# This method will prevent the screen to close automatically
screen.exitonclick()

