from dealer import Dealer
from player import Player

class Game:

    def __init__(self):
        self.player1 = Player(1)
        player2 = Player(2)
        self.players = [self.player1, player2]
        self.dealer = Dealer()

    def start_game(self):
        self.dealer.deal_card(self.players)

        for hand in self.player1.hand:
            hand.show_card()
