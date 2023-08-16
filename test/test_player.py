from src.player import Player
from src.cards import Deck
import unittest
import logging

class TestPlayer(unittest.TestCase):


    def setUp(self):
        self.deck = Deck()
        self.deck.build()
        self.player = Player(1)
        self.player.hand = self.deck.cards[:10:2]

    def test_palyer_hand(self):
        self.assertEqual(len(self.player.hand),5)

    def test_sequence_maker(self):
        self.assertEqual(len(self.player.get_sequence()), 1)

    def test_doubles(self):
        self.assertEqual(len(self.player.get_doubles()), 2)

    def test_valid_plays(self):
        self.assertEqual(len(self.player.valid_plays()), 8)
