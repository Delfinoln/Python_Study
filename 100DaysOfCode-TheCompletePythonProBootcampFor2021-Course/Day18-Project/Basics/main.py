##### Ex. 1
# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# screen = Screen()
# screen.exitonclick()

import turtle as t

tim = t.Turtle()

##### Ex. 2
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


##### Ex. 3
# corners = [3,4,5,6,7]
# color = ['red', 'green', 'purple', 'violet', 'pink', 'gray']

# for corner in corners:
#     tim.color(color[corners.index(corner)])
#     for _ in range(corner):        
#         tim.right(360/corner)
#         tim.forward(50)


#####Ex. 4 - Random Walk and random RGB color

# import random

# directions = [0, 90, 180, 270]

# #Setting line thickness, speed and color type
# tim.speed(0)
# tim.pensize(10)
# t.colormode(255)

# #Function to choose a random RGB color
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# #Random Walk
# while True:
#     tim.left(random.choice(directions))
#     tim.color(random_color())
#     tim.forward(30)
    

# screen = t.Screen()
# screen.exitonclick()


##### Ex. 5 - Draw a Spirograph
import random

#Setting line thickness, speed and color type
tim.speed(6)
tim.pensize(1)
#t.colormode()


# #Function to choose a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#Draw Spirograph
for _ in range(0,351,10):
    tim.left(_)
    tim.color(random_color())
    tim.circle(100)


screen = t.Screen()
screen.exitonclick()

