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

    def __str__(self):
        return f'{self.suit} {self.value}'

    def __repr__(self):
        return str(self)

class Deck(object):

    def __init__(self):
        self.cards = []
        self.discarded_cards = []

    def build(self, size = 1):
        '''
            Build the deck
        '''
        suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']

        self.cards = [Card(s,v) for v in range(1,14) for s in suits] * size

    def discard(self, card:Card):
        '''
            Helper function to add cards to discarded list
        '''
        self.discarded_cards.append(card)

    def shuffle(self):
        '''
            shuffle function
        '''
        random.shuffle(self.cards)
