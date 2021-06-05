from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File created')
    else:
        if website in data:
            current_data = data[website]

            messagebox.showinfo(title=f"{website} Credentials", message=f"Username: {current_data['username']}\n"
                                    f"Password: {current_data['password']}")

            pyperclip.copy(current_data['password'])

        else:
            messagebox.showinfo(title=f"{website} Credentials", message=f"There is no credentials saved for {website}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="You left some empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
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

search_button = Button(text='Search', command=search, width=14)
search_button.grid(row=1, column=2, sticky='w')

##### Creating entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

username_entry = Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2, sticky='w')
username_entry.insert(0, "dummy_email@hotmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

window.mainloop()