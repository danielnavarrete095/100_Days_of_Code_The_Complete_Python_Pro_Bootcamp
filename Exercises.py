print("Hello World!"[1:-2])
print(type(123_456_789))
print(type(str(123_456_789)))
print(3**3)

# PEMDAS
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)

#rounding
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)

score = 0
heigth = 1.8
isWinning = True
#fString
print(f"Your score is: {score}, your heigth is: {heigth}, you're winning is: {isWinning}")
# Tip calculator
# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill? "))
# percentage = int(input("What percentage tip would you like to give? "))
# num_persons = int(input("How many people to split the bill? "))
# tip = bill * (percentage / 100)
# splitted_bill = (bill + tip) / num_persons
#Formatting strings
# print("Each persohn should pay: {:.2f}".format(splitted_bill))

#ternary
odd_or_even = "odd" if 5 % 2 else "even"

#Day 4 - Random
import random
random_int = random.randint(0, 1)
print(random_int)

print(round(random.random()*5))

#Importing modules
# import my_module
# print(my_module.pi)

# from my_module import pi
# print(pi)

from my_module import pi as pie
print(pie)

my_list = ["Hello", 1, 1.52, True]
my_list.append(120.0)
# my_list.extend(range(10))
print(my_list)
print(random.choice(my_list))
print(my_list[-5])

# Sum of all even numbers from 1 to 100
total = 0
for num in range(2, 101, 2):
    total += num
print(total)

# Docstrings
def func():
    """This is a Docstring, write the description of the function
        It can be milti-line"""
    return
func()