from src.dealer import Dealer
from src.player import Player

class Game:

    def __init__(self):
        '''
            Set the players and agents of the game.
        '''
        self.player1 = Player(1)
        player2 = Player(2)
        self.players = [self.player1, player2]
        self.dealer = Dealer()

    def start_game(self):
        self.dealer.deal_card(self.players)

        self.winner = False

