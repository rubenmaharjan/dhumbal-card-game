from src.cards import Deck
from src.player import Player
from src.cards import Card

class Dealer:

    def __init__(self):
        '''
            Initialize the Dealer and deck
        '''
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.current_deck = self.deck.cards
        self.choice_card: list[Card] = []

    def deal_card(self, players:list[Player], number_of_cards:int = 5):
        '''
            Deal the cards to the players turn by turn from a shuffled deck
        '''
        for _ in range(number_of_cards):
            for player in players:
                player.hand.append(self.current_deck.pop())
        self.choice_card = [self.current_deck.pop()]
    
    def clear_choice_card(self):
        '''
            Helper method to clear the choice card and place it in the discarded section
        '''
        for card in self.choice_card:
            self.deck.discard(card)
        self.choice_card = []
