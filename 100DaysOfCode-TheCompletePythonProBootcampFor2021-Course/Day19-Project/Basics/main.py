##### Quick example on functiona as a parameter of another function

# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# def calculator(n1, n2, func):
#     return func(n1, n2)


# result = calculator(2, 3, add)
# print(result)


# ##### Using event listener to draw on screen
# import turtle

# tim = turtle.Turtle()
# screen = turtle.Screen()


# def move_forwards():
#     '''Move turtle forwards by 10 spaces'''
#     tim.forward(10)


# def move_backwards():
#     '''Move turtle backwards by 10 spaces'''
#     tim.backward(10)


# def turn_clockwise():
#     '''Turn turtle orientation by 10 degrees clockwise'''
#     tim.right(10)


# def turn_counter_clockwise():
#     '''Turn turtle orientation by 10 degrees counter-clockwise'''
#     tim.left(10)


# def clear_reset():
#     '''Clear screen and reset position'''
#     screen.reset()


# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_clockwise)
# screen.onkey(key="a", fun=turn_counter_clockwise)
# screen.onkey(key="c", fun=clear_reset)
# screen.exitonclick()


# ##### Understanding the turtle coordinate system
# import turtle

# tim = turtle.Turtle(shape='turtle')
# screen = turtle.Screen()

# screen.setup(width=500, height=400)

# # player_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
# # print(player_bet)

# tim.penup()
# tim.goto(x=-230, y=0)

# screen.exitonclick()


##### Advancing towards the final project. Creating 6 turtles and setting their positions
import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]

screen = turtle.Screen()
screen.setup(width=500, height=400)

for turtle_index in range(0,6):
    tim = turtle.Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()




