from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.configure(text=f"{new_text}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.configure(padx=20, pady=20)


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
