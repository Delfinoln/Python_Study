from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="You left some empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

##### Creating logo image
canvas=Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

##### Creating labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='e', padx=1)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky='e', padx=1)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='e', padx=1)

##### Creating buttons
add_button = Button(text='Add', width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

##### Creating entries
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

username_entry = Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2, sticky='w')
username_entry.insert(0, "dummy_email@hotmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

window.mainloop()