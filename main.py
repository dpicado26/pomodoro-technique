from tkinter import *
import math

# CONSTANTS #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
iterations = 0
timer = None


# TIMER RESET #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    main_label.config(text="Timer")
    check_boxes.config(text="")
    global iterations
    iterations = 0


# TIMER MECHANISM #
def start_timer():
    global iterations
    iterations += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if iterations % 8 == 0:
        count_down(long_break_seconds)
        main_label.config(text="Break", fg=RED)
    elif iterations % 2 == 0:
        count_down(short_break_seconds)
        main_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        main_label.config(text="Work", fg=GREEN)


# COUNTDOWN #
def count_down(count):
    minutes_count = math.floor(count / 60)
    seconds_count = count % 60
    if seconds_count < 10:
        seconds_count = f"0{seconds_count}"

    canvas.itemconfig(timer_count, text=f"{minutes_count}:{seconds_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        for _ in range(math.floor(iterations / 2)):
            checks += "✅"
        check_boxes.config(text=checks)


# UI SETUP #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, height=50, bg=YELLOW)

main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
main_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_boxes = Label(fg=GREEN, bg=YELLOW)
check_boxes.grid(column=1, row=3)
window.mainloop()
