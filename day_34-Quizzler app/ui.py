from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question Text",
                                                     font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, font=("Ariel", 12), fg="white")
        self.score_label.grid(column=1, row=0)

        yes_img = PhotoImage(file="./images/true.png")
        self.yes_button = Button(image=yes_img, command=self.checkmark, highlightthickness=0, borderwidth=0)
        self.yes_button.grid(column=0, row=2)

        no_img = PhotoImage(file="./images/false.png")
        self.no_button = Button(image=no_img, command=self.red_x, highlightthickness=0, borderwidth=0)
        self.no_button.grid(column=1, row=2)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
    def checkmark(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def red_x(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)