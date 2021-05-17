import turtle
import pandas as pd

exists = False

screen = turtle.Screen()
screen.title("U.S. States Game")

# Setting up screen
screen.setup(width=730, height=510)
screen.tracer(0)

# Adding image to the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.update()

# Reading csv file with pandas
data_frame = pd.read_csv("50_states.csv")
print(data_frame)

# Creating a writer Turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

game_is_on = True
STATES = 50
correct_states = []

while game_is_on and len(correct_states) < 50:
    # Asking user
    answer_state = screen.textinput(title=f"{len(correct_states)}/{STATES} States Correct", prompt="What's another state's name?").title()

    # Check if user's answer exists in the data frame
    if answer_state in data_frame["state"].to_list():
        exists = True

    # Write on screen the name of the state
    if exists and answer_state not in correct_states:
        correct_states.append(answer_state)
        state_x = data_frame[data_frame["state"] == answer_state]["x"]
        state_y = data_frame[data_frame["state"] == answer_state]["y"]
        writer.goto(int(state_x), int(state_y))
        writer.write(answer_state, align="center", font=("Courier", 8, "normal"))
        exists = False

print("You got all 50 states!")


screen.exitonclick()
