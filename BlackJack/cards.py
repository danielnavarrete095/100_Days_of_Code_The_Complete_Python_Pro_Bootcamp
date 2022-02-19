import random

def get_random_index(max):
    return round(random.random() * max)

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


def create_card(card_num):
    symbol_index = round(random.random()*3)
    space = " " if card_num != "10" else ""
    card = [[] for i in range(9)]
    card[0] += ('┌─────────┐')
    card[1] += ('│{}{}       │'.format(card_num, space))  # use two {} one for char, one for space or char
    card[2] += ('│         │')
    card[3] += ('│         │')
    card[4] += ('│    {}    │'.format(suits_symbols[symbol_index]))
    card[5] += ('│         │')
    card[6] += ('│         │')
    card[7] += ('│       {}{}│'.format(space, card_num))
    card[8] += ('└─────────┘')
    return card

def get_card_from_deck(deck):
    deck_size = len(deck)
    index = get_random_index(deck_size - 1)
    card = deck[index]
    deck.pop(index)
    return card