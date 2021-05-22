import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = tkinter.Label(text='I am a Label', font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
# OR
my_label.config(text="New Text")


# Button

def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)



window.mainloop()
