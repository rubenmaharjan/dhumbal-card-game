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
        '''
            The entry point of the play
        '''
        self.dealer.deal_card(self.players)

        self.winner = False

        while not self.winner:
            for player in self.players:
            #Check if the player can finish the game

                if player.can_finish():
                    print("Do you want to show your cards?")
                    print("1.Yes\n 2.No")
                    choice_finish = int(input("Enter the number: "))
                    if choice_finish == 1:
                        # Finish the game
                        self.finish_game()
                        self.winner = True
                        break
                self.play_turn(player)
                print("\nPlayer Change!!!!!!!!!!!!!!!\n")

    def play_turn(self, player:Player):
        '''
            Player turn. Asks the player to choose the card to throw and pick.
        '''

        print("Your Current Hand:")
        player.print_current_hand()
        print("    ------     ")
        print("Your Choice Cards:")
        print(self.dealer.choice_card)
        print("    ------     ")
        print("What do you want to play?")
        valid_plays =  player.valid_plays()
        for index, valid in enumerate(valid_plays,1):
            print(index,": ", valid)
        num = input("Enter the number: ")
        while not Game.is_integer(num, 1, len(valid_plays)):
            num = input("Enter the number: ")
        num = int(num)
        throw = valid_plays[num-1]

        for card in throw:
            player.hand.remove(card)

        print("\n")
        print("Pick from Choice Cards of Deck?")
        print("1: Deck")
        for index, card in enumerate(self.dealer.choice_card, 2):
            print(index, ": ", card)

        choice_pick = input("Enter the number: ")
        while not Game.is_integer(choice_pick, 1, len(self.dealer.choice_card)+1):
            choice_pick = input("Enter the number: ")
        choice_pick = int(choice_pick)
        print("\n")
        if choice_pick == 1:
            player.hand.append(self.dealer.current_deck.pop())
        else:
            player.hand.append(self.dealer.choice_card.pop(choice_pick-2))
        player.print_current_hand()

        # Clear out the choice card as we are ending this players turn
        self.dealer.clear_choice_card()

        # Add new set of choice card for next player
        self.dealer.choice_card = throw

    def finish_game(self):
        min_score = 100
        winner_player_id = -1
        for player in self.players:
            player.finish_game()
            if player.score < min_score:
                min_score = player.score
                winner_player_id = player.player_id 

        print("Winner : Player ", winner_player_id)
        print("Winner Score :", min_score)

    @staticmethod
    def is_integer(input_number, start, end ):
        try:
            num = int(input_number)
            print("Choice : ", num, start, end)
            if num < start or num > end:
                print("Invalid Choice : ", input_number)
                return False
            return True
        except ValueError:
            print("Expcting a number but got: ", input_number)
            return False
