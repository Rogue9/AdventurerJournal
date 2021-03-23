from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.question_field = Canvas()
        self.question_text= self.question_field.create_text(
            150,
            125,
            width=266,
            text="show question text",
            font=QUESTION_FONT,
            fill=THEME_COLOR)

        self.question_field.grid(row=1, column=0, columnspan=2)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR,command=self.answer_true)
        self.true.grid(row=2, column=0)
        self.false = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.answer_false)
        self.false.grid(row=2, column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.question_field.config(bg='white', width=300, height=250)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_field.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.question_field.itemconfig(self.question_text,
                                           text=f"You've reached the end of the quiz. Your final score was "
                                                f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_field.config(bg="green")
        else:
            self.question_field.config(bg="red")
        self.window.after(1000, self.get_next_question)