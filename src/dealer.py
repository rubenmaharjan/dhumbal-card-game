from src.cards import Deck
from src.player import Player
from src.cards import Card

class Dealer:

    def __init__(self):
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.current_deck = self.deck.cards
        self.choice_card: list[Card] = []

    def deal_card(self, players:list[Player], number_of_cards:int = 5):
        for _ in range(number_of_cards):
            for player in players:
                player.hand.append(self.current_deck.pop())
        self.choice_card = [self.current_deck.pop()]
