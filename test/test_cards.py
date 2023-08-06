from src.cards import Card, Deck
import unittest

class TestCards(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck_size = 1
        self.deck.build(self.deck_size)

    def test_deck_size(self):
        self.assertEqual(len(self.deck.cards), 52)
        self.deck_size = 2
        self.deck.build(self.deck_size)
        self.assertEqual(len(self.deck.cards), 52 * self.deck_size)

