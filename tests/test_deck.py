import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from game.deck import Deck

class testDeck(unittest.TestCase):
    def test_deck_length(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_draw(self):
        deck = Deck()
        hand = []
        hand.append(deck.draw())
        self.assertEqual(len(hand), 1)
        hand.append(deck.draw())
        self.assertEqual(len(hand), 2)

    def test_draw_card_correct(self):
        deck = Deck()
        card = deck.draw()
        self.assertIn(card['suit'], ['Hearts', 'Diamonds', 'Spades', 'Clubs'])
        self.assertIn(card['rank'], ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
        self.assertIn('value', card)

    def test_get_suit_rank_valid(self):
        deck = Deck()
        rank, suit = deck.get_suit_rank("10 of Hearts")
        self.assertEqual(rank, "10")
        self.assertEqual(suit, "Hearts")

        rank, suit = deck.get_suit_rank("A of Spades")
        self.assertEqual(rank, "A")
        self.assertEqual(suit, "Spades")

    def test_get_value_valid_ranks(self):
        deck = Deck()
        self.assertEqual(deck.get_value('J'), 11)
        self.assertEqual(deck.get_value('Q'), 12)
        self.assertEqual(deck.get_value('K'), 13)
        self.assertEqual(deck.get_value('A'), 14)

    #edge cases
    def test_get_value_invalid_rank(self):
        deck = Deck()
        self.assertEqual(deck.get_value('C'), 0) 
        self.assertEqual(deck.get_value('B'), 0)   