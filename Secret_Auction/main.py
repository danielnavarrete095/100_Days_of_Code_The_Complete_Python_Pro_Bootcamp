import os
from art import logo

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

bidders = {}

print(logo)
print("Welcome to the secret auction program.")
more_bidders = "yes"
while more_bidders == "yes" or more_bidders == "y":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'. ").lower()
    if more_bidders == "yes" or more_bidders == "y":
        clearConsole()

highest_bid = 0
winner = ""
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        winner = key
print(f"The winner is {winner} with a bid of ${highest_bid}")