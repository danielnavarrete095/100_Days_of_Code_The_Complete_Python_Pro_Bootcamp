############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import time
import os
import random
import art
import cards

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def getRandomIndex():
    return round(random.random() * 12)

def printGame():
    clearConsole()
    print("Dealer cards:")
    cards.print_cards(dealer_cards)
    print("Your cards:")
    cards.print_cards(user_cards)


print(art.logo)

print("Press enter to start game")
# cards.print_cards(cards.hidden_card, cards.hidden_card, cards.hidden_card, cards.hidden_card)
input()

# Get 1 dealer card
# Create dealer first card and second will be hidden
dealer_cards = []
dealer_cards.append(cards.create_card(getRandomIndex()))
dealer_cards.append(cards.hidden_card)

# Now get user cards
user_cards = []
for i in range(2):
    user_cards.append(cards.create_card(getRandomIndex()))

printGame()
print("Type 'h' to hit, type 's' to stand")
option = input()
# If user selected the option to draw another card
if option.lower() == "h":
    # add another card to users
    user_cards.append(cards.create_card(getRandomIndex()))

# If user selected the option to stand
elif option.lower() == "s":
    # Reveal dealer's second card
    dealer_cards.pop(1)
    dealer_cards.append(cards.create_card(getRandomIndex()))

printGame()
# cards.print_card(cards.hidden_card)
# cards.print_card(cards.dealer_card)
# time.sleep(2)
# clearConsole()
# cards.print_2_cards(cards.dealer_card, cards.hidden_card)

