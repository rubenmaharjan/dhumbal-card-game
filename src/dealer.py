from cards import Deck
from player import Player

class Dealer:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.current_deck = self.deck.cards

    def deal_card(self, player:Player):
        player.hand.append(self.current_deck.pop())
