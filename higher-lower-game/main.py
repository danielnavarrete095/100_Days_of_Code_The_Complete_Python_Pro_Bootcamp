import random
import os
from tkinter import W
from game_data import data
from art import game_name, vs

def get_random_index(max):
    return round(random.random() * max)

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def get_profile():
    index = get_random_index(len(data))
    profile = data[index]
    data.pop(index)
    return profile

def get_higher_follower_count(profileA, profileB):
    if profileA["follower_count"] > profileB["follower_count"]:
        return profileA
    else:
        return profileB


def main():
    score = 0
    profileA = get_profile()
    profileB = None
    while(True):
        clear_console()
        print(game_name)
        if profileB != None:
            print(f"You are right! Current score: {score}.")

        profileB = get_profile()

        # print(profileA)
        # print(profileB)
        print(f"Compare A: {profileA['name']}, a {profileA['description']}, from {profileA['country']}.")
        print(vs)
        print(f"Against B: {profileB['name']}, a {profileB['description']}, from {profileB['country']}.")

        winner_profile = get_higher_follower_count(profileA, profileB)

        selected_profile = ""
        while(True):
            print("Who has more followers? Type 'A' or 'B': ", end=" ")
            option = input().lower()
            if option == "A" or option == "a":
                selected_profile = profileA
                break
            elif option == "B" or option == "b":
                selected_profile = profileB
                break
            else:
                print("Select a valid option!")

        if selected_profile == winner_profile:
            score += 1
            print(f"You are right! Current score: {score}.")
            profileA = selected_profile
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break


if __name__ == '__main__':
    main()