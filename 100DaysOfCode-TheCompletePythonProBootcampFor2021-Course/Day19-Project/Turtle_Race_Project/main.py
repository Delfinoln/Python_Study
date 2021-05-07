import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen = turtle.Screen()
screen.setup(width=500, height=400)

player_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if player_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            winning_color = turtle.pencolor()
            if winning_color == player_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on = False
            break

        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)


screen.exitonclick()