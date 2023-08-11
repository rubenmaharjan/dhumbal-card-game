import random

class Card(object):

    def __init__(self, suit, value):
        '''
            Card object that defines suit and value
        '''
        self.suit = suit
        self.value = value

    def show_card(self):
        print(self.suit," , ", self.value)

class Deck(object):

    def __init__(self):
        self.cards = []
        self.discarded_cards = []

    def build(self, size = 1):
        suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']

        self.cards = [Card(s,v) for v in range(1,14) for s in suits] * size

    def discard(self, card:Card):
        self.discarded_cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
