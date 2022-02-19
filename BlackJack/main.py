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
from traceback import print_tb
import art
import cards
from Player import Player

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_game():
    clear_console()
    print("{0} cards:".format(Dealer.name))
    cards.print_cards(Dealer.cards)
    print("{0} cards:".format(User.name))
    cards.print_cards(User.cards)

User = Player("User")
Dealer = Player("Dealer")
Num_of_decks = 4
Deck = cards.cards * Num_of_decks
clear_console()
print(art.logo)

print("Press enter to start game")
# User.add_card([cards.create_card(0), 0])
# User.compute_score()
# User.add_card([cards.create_card(0), 0])
# User.compute_score()
# cards.print_cards(cards.hidden_card, cards.hidden_card, cards.hidden_card, cards.hidden_card)
input()

# Get 1 Dealer card
# Create Dealer first card and second will be hidden
Dealer.add_card(Deck)
Dealer.add_card(Deck, hidden=True)

# Now get User cards
User.add_card(Deck)
User.add_card(Deck)


while(True):
    print_game()
    print("Type 'h' to hit, type 's' to stand")
    option = input()
    # If User selected the option to draw another card
    if option.lower() == "h":
        # add another card to users
        User.add_card(Deck)
    # If User selected the option to stand
    elif option.lower() == "s":
        break


# Reveal Dealer's second card
Dealer.remove_card()
Dealer.add_card(Deck)
Dealer.compute_score()
User.compute_score()
# Dealer should try to beat user
if User.score <= 21: # This would mean user already lost
    if Dealer.score < User.score:
        # Dealer should keep drawing cards if < 21
        while Dealer.score < 21:
            Dealer.add_card(Deck)
            Dealer.compute_score()
print_game()
User.compute_score()
Dealer.compute_score()
User.print_score()
Dealer.print_score()
if User.score > 21:
    print("BUST!\nYou loose!🙁");
elif Dealer.score > 21:
    print("You win!🙂");
else:
    if User.score > Dealer.score:
        print("You win!🙂");
    elif User.score < Dealer.score:
        print("You loose!🙁");
    else:
        print("Draw!😐")
