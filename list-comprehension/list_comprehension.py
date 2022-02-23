from numpy import short


def main():
    # This:
    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        new_list.append(n + 1)
    print(new_list)

    # Is equals to this:
    new_list_1 = [item + 1 for item in numbers]
    print(new_list_1)

    name = "Daniel"
    name_list = [letter for letter in name]
    print(name_list)

    range_list = [num * 2 for num in range(1, 5)]
    print(range_list)

    even_numbers = [num for num in range(1, 100) if not num % 2]
    odd_numbers = [num for num in range(1, 100) if num % 2]
    print(even_numbers)
    print(odd_numbers)

    names = ["Daniel", "Melissa", "Edith", "Angela", "David", "Ian", "Alex", "Caroline", "Dave", "Beth"]
    short_names = [name.upper() for name in names if len(name) <= 5]
    print(short_names)

    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [num * num for num in numbers]
    print(squared_numbers)

    # Instructions
    # Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

    # You are going to create a list called result which contains the numbers that are common in both files.
    # IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

    # create a list for wach file
    numbers = []
    # Read each file and fill the lists
    files = ("file1.txt", "file2.txt")
    for i, file_name in enumerate(files):
        numbers.append([])
        with open(file_name) as file:
            lines = file.readlines()
            for line in lines:
                num = int(line)
                numbers[i].append(num)
    print(numbers)
    result = [num for num in numbers[0] if num in numbers[1]]
    print(result)
if __name__ == '__main__':
    main()