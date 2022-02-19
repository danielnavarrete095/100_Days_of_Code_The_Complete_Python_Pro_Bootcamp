import random
art = r"""
     __                    _                     ___                         _                   ___                        
  /\ \ \ _   _  _ __ ___  | |__    ___  _ __    / _ \ _   _   ___  ___  ___ (_) _ __    __ _    / _ \ __ _  _ __ ___    ___ 
 /  \/ /| | | || '_ ` _ \ | '_ \  / _ \| '__|  / /_\/| | | | / _ \/ __|/ __|| || '_ \  / _` |  / /_\// _` || '_ ` _ \  / _ \
/ /\  / | |_| || | | | | || |_) ||  __/| |    / /_\\ | |_| ||  __/\__ \\__ \| || | | || (_| | / /_\\| (_| || | | | | ||  __/
\_\ \/   \__,_||_| |_| |_||_.__/  \___||_|    \____/  \__,_| \___||___/|___/|_||_| |_| \__, | \____/ \__,_||_| |_| |_| \___|
                                                                                       |___/                                
"""
def main():
    guess_number = round(random.random() * 101)
    print(f"Guess number: {guess_number}")
    print(art)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking in a number between 1 and 100.\n")
    print("Choose a difficulty. Type 'easy' or 'hard': ")
    while(True):
        option = input()
        if option.lower() == "e" or option.lower() == "easy":
            attempts = 10
            break
        elif option.lower() == "h" or option.lower() == "hard":
            attempts = 5
            break
        else:
            print("Select a valid option!")

    win = False
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        while(True):
            print("Make a guess:", end=" ")
            try:
                guess = int(input())
                break
            except ValueError:
                print("Please write numbers only")
        if guess > guess_number:
            print("Too high!")
        elif guess < guess_number:
            print("Too low!")
        else:
            win = True
            break
        attempts -= 1
    if win:
        print("You guessed correctly!")
    else:
        print("You've run out of guesses, you lose.")

if __name__ == '__main__':
    main()