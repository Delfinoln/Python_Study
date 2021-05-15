import turtle
import character
import car
import time
import scoreboard

# Creating a screen object
screen = turtle.Screen()

# Setting up screen atributes
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating a Character
player = character.Character()

# Creating a screen listener
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_down, "Down")

# Creating scoreboard objet
scoreboard = scoreboard.Scoreboard()

is_game_on = True
counter = 0

cars = car.Car()
cars.cars_list.append(cars)

while is_game_on:
    screen.update()
    cars.move()
    time.sleep(cars.pace)
    counter += 1
    if counter == 6:
        counter = 0
        (cars.cars_list.append(car.Car()))
    if player.ycor() == 280:
        cars.pace *= 0.8
        scoreboard.level += 1
        scoreboard.rewrite()
        player.reset()
    for one_car in cars.cars_list:
        if player.distance(one_car) < 20:
            is_game_on = False
            scoreboard.game_over()

# In order to not close the window
screen.exitonclick()
