from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.configure(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.configure(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #!Code invalid i modified it below
    # if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    #     count_down(work_sec)
    # elif reps == 2 or reps == 4 or reps == 6:
    #     count_down(short_break_sec)
    # elif reps == 8:
    #     count_down(long_break_sec)
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        sign = ""
        work_sesh = math.floor(reps/2)
        for _ in range(work_sesh):
            sign += "✔️"
        checkmark.configure(text=sign)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.configure(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(
    FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="pomodoro_app/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", borderwidth=0.3,
                      highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

rest_button = Button(text="Reset", borderwidth=0.3,
                     highlightthickness=0, command=reset_timer)
rest_button.grid(row=2, column=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)


window.mainloop()
