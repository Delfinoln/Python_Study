import turtle

# Creating a Screen object called screen
screen = turtle.Screen()

# Setting up screen elements
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


# This method will prevent the screen to close automatically
screen.exitonclick()
