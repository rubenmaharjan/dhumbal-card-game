from src.game import Game
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_start_game(self):
        self.game.start_game()
