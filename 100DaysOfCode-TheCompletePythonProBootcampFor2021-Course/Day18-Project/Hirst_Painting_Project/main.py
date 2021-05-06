import colorgram
import random
import turtle

# Extracting the colors from an image
colors = colorgram.extract(
    r'C:\Users\delfino\OneDrive\local_repository\Python_Study\100DaysOfCode-TheCompletePythonProBootcampFor2021-Course\Day18-Project\Hirst_Painting_Project\image.jpg',
    30)

colors_list = []
# Creating a List os Tuples, each containing a different color from the image
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    # After analyzing the colors content, I decided to erase colors that are simmilar to white
    if r + g + b < 720:
        new_color = (r, g, b)
        colors_list.append(new_color)

# Set the color mode os module turtle
turtle.colormode(255)

# Creating a turtle Object named tim
tim = turtle.Turtle()
tim.hideturtle()
tim.speed(0)

# Creating a screen Object named screen
screen = turtle.Screen()

# Setting up screen elements
screen.screensize(1200, 1200)


# Create a function to draw a line
def draw_line():
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()


# Create a function to change line
def change_line():
    tim.penup()
    tim.left(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)


# Draw a Hirst Painting
for _ in range(10):
    draw_line()
    change_line()

screen.exitonclick()