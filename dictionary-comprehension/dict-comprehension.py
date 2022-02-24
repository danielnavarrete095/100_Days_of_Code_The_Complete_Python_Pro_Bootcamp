import random
def main():
    students = ["Daniel", "Melissa", "Edith", "Angela", "David", "Ian", "Alex", "Caroline", "Dave", "Beth"]
    # names_dict = {}
    
    students_scores = {student:random.randint(50, 100) for student in students}
    print(students_scores)
    print(students_scores["Daniel"])

    passed_students = {name:score for (name, score) in students_scores.items() if score >= 70}
    print(passed_students)
    failed_students = {name:score for (name, score) in students_scores.items() if score < 70}
    print(failed_students)
    
    # Instructions
    # You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

    # Try Googling to find out how to convert a sentence into a list of words.

    # Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    result = {word:len(word) for word in sentence.split()}
    print(result)


if __name__ == '__main__':
    main()