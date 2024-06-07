from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- Choose Random Entry ------------------------------- #
def new_word():
    return choice(data_dict)

# ---------------------------- Import CSV ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    df = pandas.DataFrame.from_dict(data_dict, orient="columns")
    df.to_csv("./data/words_to_learn.csv",header=True, index=False)
else:
    data_dict = data.to_dict(orient="records")
random_entry = new_word()

# ---------------------------- Countdown Timer ------------------------------- #
def new_card():
    global random_entry, flip_timer
    random_entry = new_word()
    canvas.itemconfig(background, image=first_bg)
    canvas.itemconfig(lang_name, text="French", fill="black")
    canvas.itemconfig(translation, text=random_entry["French"], fill="black")
    flip_timer = window.after(3000, show_answer)

def show_answer():
    canvas.itemconfig(background, image=second_bg)
    canvas.itemconfig(lang_name, text="English", fill="white")
    canvas.itemconfig(translation, text=random_entry["English"], fill="white")

# ---------------------------- Right Answer ------------------------------- #
def correct_answer():
    global random_entry, flip_timer
    window.after_cancel(flip_timer)
    data_dict.remove(random_entry)
    df = pandas.DataFrame.from_dict(data_dict, orient="columns")
    df.to_csv("./data/words_to_learn.csv",header=True, index=False)
    new_card()


# ---------------------------- Wrong Answer ------------------------------- #
def wrong_answer():
    global flip_timer
    window.after_cancel(flip_timer)
    new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
first_bg = PhotoImage(file="./images/card_front.png")
second_bg = PhotoImage(file="./images/card_back.png")

background = canvas.create_image(0, 0, anchor=NW, image=first_bg)
canvas.grid(column=0, row=0, columnspan=2)
lang_name = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
translation = canvas.create_text(400, 263, text=random_entry["French"], font=("Ariel", 60, "bold"))
flip_timer = window.after(3000, show_answer)

#Buttons
yes_img = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_img, command=correct_answer, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)
yes_button.grid(column=0, row=2)

no_img = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_img, command=wrong_answer, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)
no_button.grid(column=1, row=2)


window.mainloop()
