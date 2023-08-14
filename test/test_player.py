from src.player import Player
from src.cards import Deck
import unittest
import logging

class TestPlayer(unittest.TestCase):


    def setUp(self):
        self.deck = Deck()
        self.deck.build()
        self.player = Player(1)
        self.player.hand = self.deck.cards[:20:4]

    def test_palyer_hand(self):
        self.assertEqual(len(self.player.hand),5)

    def test_sequence_maker(self):
        self.assertGreaterEqual(len(self.player.get_sequence()), 1)
