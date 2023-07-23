from tkinter import *


def calculator():
    miles_value = float(input.get())
    km_value = miles_value * 1.609
    kilometer_value.configure(text=f"{km_value}")


window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width=500, height=300)
window.configure(padx=20, pady=20)

# empty = Label(text="", font=("Arial", 12))
# empty.grid(column=0, row=0)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)

equals = Label(text="is equal to", font=("Arial", 12))
equals.grid(column=0, row=1)


kilometer_value = Label(text="0", font=("Arial", 12))
kilometer_value.grid(column=1, row=1)


kilometer = Label(text="Km", font=("Arial", 12))
kilometer.grid(column=2, row=1)


calculate_button = Button(text="Calculate", command=calculator)
calculate_button.grid(column=1, row=2)


window.mainloop()
