from src.game import Game

game = Game()
game.start_game()
print(game.player1.hand)
print(game.player1.get_sequence())
