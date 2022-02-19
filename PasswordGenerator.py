import random
# letters_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers_str = "0123456789"
# symbols_str = "!#$%&()*+"

# letters = list(letters_str)
# numbers = list(numbers_str)
# symbols = list(symbols_str)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print(letters)
# print(numbers)
# print(symbols)

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbolds would you like?\n"))
total_chars = num_letters + num_numbers + num_symbols
remaining_total = total_chars
password = ""
remaining_each = [num_letters, num_numbers, num_symbols]
list_of_chars = [letters, numbers, symbols]
# for _ in range(total_chars):
while remaining_total:
    #Decide if you want letter(0)/symbol(1)/number(2)
    type_of_char = random.randint(0, 2)
    #Check if we still have remaining chars of that type
    if remaining_each[type_of_char] > 0:
        # select a random char based on previous choice
        password += random.choice(list_of_chars[type_of_char])
        # password += list_of_chars[type_of_char][random.randint(0, len(list_of_chars[type_of_char]) - 1)]
        remaining_each[type_of_char] -= 1
        remaining_total -= 1
print(password)

# Better way: add all the characters in any sequence and then shuffle everything
password_list = []
num_list = [num_letters, num_numbers, num_symbols]
for idx, num in enumerate(num_list):
    for _ in range(num):
        password_list += random.choice(list_of_chars[idx])
random.shuffle(password_list)
password = "".join(password_list)
print(password)


