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

        while not self.winner:
            for player in self.players:
                self.play_turn(player, self.dealer.choice_card)

    def play_turn(self, player:Player, choice_card:list):
        print("What do you want to play?")
        valid_plays =  player.valid_plays()
        for index, valid in enumerate(valid_plays,1):
            print(index,": ", valid)
        num = int(input("Enter the number: "))
        #TODO Check fi the num is valid
        throw = valid_plays[num-1]


