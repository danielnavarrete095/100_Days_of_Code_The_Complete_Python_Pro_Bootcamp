import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# print(rock, paper, scissors)
options = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0 , 2)

# print(user_choice)
# print(computer_choice)
err = 0
if user_choice == computer_choice:
    result = "You draw"
elif user_choice == 0:
    if computer_choice == 1:
        result = "You lose"
    if computer_choice == 2:
        result = "You win"
elif user_choice == 1:
    if computer_choice == 0:
        result = "You win"
    if computer_choice == 2:
        result = "You lose"
elif user_choice == 2:
    if computer_choice == 0:
        result = "You lose"
    if computer_choice == 1:
        result = "You win"
else:
    result = "You typed an invalid number, you lose!"
    err = 1
if(not err):
    print(options[user_choice])
    print("Computer chose:")
    print(options[computer_choice])
print(result)

