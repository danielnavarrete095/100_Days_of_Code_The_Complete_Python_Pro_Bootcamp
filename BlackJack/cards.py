import random

suits_symbols = ['♠', '♦', '♥', '♣']
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_values = {
        'A': [1, 11],  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

dealer_card = [[] for i in range(9)]
dealer_card[0] += ('┌─────────┐')
dealer_card[1] += ('│{}{}       │'.format(cards[0], " "))  # use two {} one for char, one for space or char
dealer_card[2] += ('│         │')
dealer_card[3] += ('│         │')
dealer_card[4] += ('│    {}    │'.format(suits_symbols[0]))
dealer_card[5] += ('│         │')
dealer_card[6] += ('│         │')
dealer_card[7] += ('│       {}{}│'.format(" ", cards[0]))
dealer_card[8] += ('└─────────┘')



hidden_card = [
    ['┌─────────┐'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['│░░░░░░░░░│'],
    ['└─────────┘']
]

def print_card(card):
    print('\n'.join([''.join(line) for line in card]))

def print_2_cards(card1, card2):
    big_space = list("    ")
    multi_card = [[] for i in range(9)]   
    for i, line in enumerate(multi_card):
        multi_card[i] = card1[i] + big_space + card2[i]
    print_card(multi_card)

# Single cards parameters
def print_cards(*cards):
    big_space = list("    ")
    multi_card = [[] for i in range(9)]
    num_of_cards = len(cards)
    for i, line in enumerate(multi_card):
        for j, card in enumerate(cards):
            multi_card[i] += card[i]
            if j < num_of_cards - 1:
                multi_card[i] += big_space
    print_card(multi_card)

# card list parameter
def print_cards(cards):
    big_space = list("    ")
    multi_card = [[] for i in range(9)]
    num_of_cards = len(cards)
    for i, line in enumerate(multi_card):
        for j, card in enumerate(cards):
            multi_card[i] += card[i]
            if j < num_of_cards - 1:
                multi_card[i] += big_space
    print_card(multi_card)


def create_card(card_index):
    symbol_index = round(random.random()*3)
    space = " " if cards[card_index] != "10" else ""
    card = [[] for i in range(9)]
    card[0] += ('┌─────────┐')
    card[1] += ('│{}{}       │'.format(cards[card_index], space))  # use two {} one for char, one for space or char
    card[2] += ('│         │')
    card[3] += ('│         │')
    card[4] += ('│    {}    │'.format(suits_symbols[symbol_index]))
    card[5] += ('│         │')
    card[6] += ('│         │')
    card[7] += ('│       {}{}│'.format(space, cards[card_index]))
    card[8] += ('└─────────┘')
    return card