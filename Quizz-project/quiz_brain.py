class QuizzBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(answer, question.answer)
    def still_has_questions(self):
        return len(self.questions_list) > self.question_number

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"The current score is {self.score}/{self.question_number}")
        else:
            print("Wrong asnwer")