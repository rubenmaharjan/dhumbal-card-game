from cards import Card

class Player:

    def __init__(self, player_id:int):
        self.player_id: int = player_id
        self.hand:list[Card] = []
        self.score = 100

    def get_player_id(self) -> int:
        '''
            Return Player's id
        '''
        return self.player_id

    def print_current_hand(self):
        '''
            Print the players current hand
        '''
        for card in self.hand:
            print(card.suit, " ", card.value)

