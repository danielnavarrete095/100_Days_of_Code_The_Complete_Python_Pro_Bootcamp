import random
import os
from hangman_graphics import graphics, logo
from hangman_words import words as word_list

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

lives = 6
# Randomly choose a word
chosen_word = random.choice(word_list)
chosen_word_list = ['_'] * len(chosen_word)
already_guessed = []

clearConsole()
print(logo)
# print(chosen_word)
for _ in chosen_word_list:
    print(_, end=" ")
print()

while('_' in chosen_word_list):
    # Ask the user to guess a letter
    # print("Lives: ", lives)
    print(graphics[-lives-1])
    guess = input("Guess a letter: ").lower()
    clearConsole()
    print(logo)
    if not guess in already_guessed:
        already_guessed += guess
        #Check if the letter is contained in the chosen word
        found = False
        for idx, letter in enumerate(chosen_word):
            if guess == letter:
                chosen_word_list[idx] = guess
                found = True
        if not found:
            print(f'Letter {guess} not in the word!')
            lives -= 1

        for _ in chosen_word_list:
            print(_, end=" ")
        print()

        if lives == 0:
            break
    else:
        print(f'Already guessed {guess}')
        for _ in chosen_word_list:
            print(_, end=" ")
        print()

print(graphics[-lives-1])

if lives == 0:
    print("You lose")
    print(f"Correct answer was: {chosen_word}")
else:
    print("You win!")
