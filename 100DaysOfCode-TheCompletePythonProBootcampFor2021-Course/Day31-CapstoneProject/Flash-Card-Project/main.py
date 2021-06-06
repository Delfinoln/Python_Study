from tkinter import *
import pandas as pd
import random 

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# ---------------------------- CREATE words_to_learn.csv ------------------------------- #
def is_known():
    data_dict.remove(current_card)
    df = pd.DataFrame(data_dict)
    df = df.to_csv("data\\words_to_learn.csv", index=False)

    next_card()


# ---------------------------- SHOW NEXT CARD ------------------------------- #
def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)

    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Creating canvas
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images\\card_front.png")
card_back_image = PhotoImage(file="images\\card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons
wrong_image = PhotoImage(file="images\\wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images\\right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


# ---------------------------- GETTING DATA ------------------------------- #
try:
    data = pd.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data\\french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
next_card()



window.mainloop()