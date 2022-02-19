from cards import get_card_from_deck
import cards
import random

# def getRandomIndex():
#     return round(random.random() * 12)

class Player:    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.values = []
        self.cards = []

    def add_card(self, deck, card = None, hidden = False):
        if hidden == False:
            if card == None:
                card_from_deck = get_card_from_deck(deck)
                self.cards.append(cards.create_card(card_from_deck))
                self.values.append(cards.card_values[card_from_deck])
            else:
                self.cards.append(card[0])
                self.values.append(cards.card_values[cards.cards[card[1]]])
        else:
            self.cards.append(cards.hidden_card)

    def remove_card(self):
        # If the card was hidden, don't need to remove a value
        if len(self.values) == len(self.cards):
            self.values.pop()
        # Remove a card, which can be a hidden one
        self.cards.pop()

    def compute_score(self):
        self.score = 0
        for value in self.values:
            if type(value) is list:
                if self.score + value[1] <= 21:
                    self.score += value[1]
                else:
                    self.score += value[0]
            else:
                self.score += value

    def print_score(self):
        print("{0} score: {1}".format(self.name, self.score))