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

    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    weather_f = {day:temp* 9 / 5 + 32 for (day, temp) in weather_c.items()}
    print(weather_f)

    print(f"students_scores: {students_scores}")
    print(f"students: {students}")
    scores = [score for (student, score) in students_scores.items()]
    print(f"scores: {scores}")
    student_dict = {
        "student": students,
        "score": scores
    }
    print(student_dict)

    # Looping through dictionaries:
    for (key, value) in student_dict.items():
        print(value)

    import pandas
    student_data_frame = pandas.DataFrame(student_dict)
    # print(student_data_frame)

    # for (key, value) in student_data_frame.items():
    #     # print(key)
    #     print(value)
    
    # Loop through rows of a data frame
    for(index, row) in student_data_frame.iterrows():
        # print(index)
        # print(row)
        if row.student == "Daniel":
            print(row)
    
if __name__ == '__main__':
    main()