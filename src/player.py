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

    # TODO Implement the function
    def valid_plays(self):
        '''
            Return the players valid moves
        '''
        return

    # TODO Implement the function
    def finish_game(self):
        '''
            Finish the game by showing your hand
            Need to validate the hand. 
            total needs to be less than 6
        '''
        return

