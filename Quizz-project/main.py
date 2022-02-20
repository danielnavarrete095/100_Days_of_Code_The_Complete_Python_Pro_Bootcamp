from data import question_data
from question import Question
from quiz_brain import QuizzBrain
def main():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))
    # print(question_bank)
    quizz = QuizzBrain(question_bank)
    while(quizz.still_has_questions()):
        quizz.next_question()
    print("You've completed the quiz!")
    print(f"Your final score was: {quizz.score}/{quizz.question_number}")
if __name__ == '__main__':
    main()