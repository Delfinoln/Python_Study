import turtle
import character
import car

# Creating a screen object
screen = turtle.Screen()

# Setting up screen atributes
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating a Character
player = character.Character()
car = car.Car()

# Creating a screen listener
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_down, "Down")

is_game_on = True

while is_game_on:
    screen.update()


# In order to not close the window
screen.exitonclick()