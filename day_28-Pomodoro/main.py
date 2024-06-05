from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 8
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    checkmarks.config(text="")
    header.config(text="Timer", fg=GREEN)
    global reps
    reps = 8
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1:
        header.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps = 8
    elif reps % 2 == 1:
        header.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        reps -= 1
    else:
        header.config(text="Work", fg=GREEN)
        count_down(work_sec)
        reps -= 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps == 0 or reps == 8:
            checkmarks.config(text="✅✅✅✅")
        elif reps >= 7:
            checkmarks.config(text="")
        elif reps >= 5:
            checkmarks.config(text="✅")
        elif reps >= 3:
            checkmarks.config(text="✅✅")
        elif reps >= 1:
            checkmarks.config(text="✅✅✅")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#Label
header = Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME,40,"bold"))
header.config(padx=0,pady=0)
header.grid(column=1, row=0)

#Buttons

start_button = Button(text="Start", command=start, highlightthickness=0)
reset_button = Button(text="Reset", command=reset, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

#checkmark
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
checkmarks.config(padx=0,pady=0)
checkmarks.grid(column=1, row=3)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="25:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1, row=1)




window.mainloop()