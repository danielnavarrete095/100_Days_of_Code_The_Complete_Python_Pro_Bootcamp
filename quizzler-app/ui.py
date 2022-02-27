from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(fg="white", font=("Arial", 15, "italic"), text="Score: 0", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)
        self.canvas_text = self.canvas.create_text(150, 125, text="Question goes here", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=290)

        self.true_img = PhotoImage(file = r"images\true.png")
        self.true = Button(image=self.true_img, highlightthickness=0, borderwidth=0, padx=20, pady=20, command=self.true_pressed)
        self.true.grid(column=0, row=2)
        self.false_img = PhotoImage(file = r"images\false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, borderwidth=0, padx=20, pady=20, command=self.false_pressed)
        self.false.grid(column=1, row=2)
        
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text = q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

        