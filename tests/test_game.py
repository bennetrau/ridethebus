import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from game.game import RideTheBus

class testRideTheBus(unittest.TestCase):

    def test_round1_color_guess(self):
        self.game = RideTheBus()
        result, card = self.game.game(1, 'red')
        self.assertIn(result, ['red', 'black'])
        self.assertIn('suit', card)

    def test_round2_high_low_logic(self):
        self.game = RideTheBus()
        self.game.player.cards = [{'value': 10}]
        result, card = self.game.game(2, 'high')
        self.assertIn(result, ['high', 'low'])

    def test_round2_equal_cards(self):
        self.game = RideTheBus()
        self.game.player.cards = [{'value': 7}]
        self.game.deck.cards.append('7 of Hearts')
        result, card = self.game.game(2, 'low')
        self.assertEqual(card['value'], 7)
        self.assertEqual(result, 'high')  

    def test_round3_between_logic(self):
        self.game = RideTheBus()
        self.game.player.cards = [{'value': 4}, {'value': 10}]
        result, card = self.game.game(3, 'between')
        self.assertIn(result, ['between', 'outside'])

    def test_round3_edge_between_equal(self):
        self.game = RideTheBus()
        self.game.player.cards = [{'value': 7}, {'value': 7}]
        self.game.deck.cards.append('7 of Diamonds') 
        result, card = self.game.game(3, 'between')
        self.assertEqual(result, 'between')

    def test_round4_correct_suit_guess(self):
        self.game = RideTheBus()
        self.game.deck.cards.append('J of Clubs')
        result = self.game.game(4, 'Clubs')
        self.assertEqual(result, 'WINNNNNNEEEERRRRR')

    def test_round4_wrong_suit_guess(self):
        self.game = RideTheBus()
        self.game.deck.cards.append('9 of Hearts')
        result = self.game.game(4, 'Spades')
        self.assertEqual(result, 'You lost')

    def test_invalid_round_number(self):
        self.game = RideTheBus()
        result, card = self.game.game(5, 'red')
        self.assertFalse(result)
        self.assertIn('display', card) 