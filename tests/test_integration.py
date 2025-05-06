import unittest
from game.game import RideTheBus

class TestRideTheBusIntegration(unittest.TestCase):
    def setUp(self):
        self.game = RideTheBus()

    def test_round_1_returns_color_and_card(self):
        result, card = self.game.game(1, 'red')
        self.assertIn(result, ['red', 'black'])
        self.assertIn('suit', card)

    def test_round_2_uses_first_card_to_compare(self):
        self.game.game(1, 'red')  # First card stored
        result, card = self.game.game(2, 'high')  # Second card compared
        self.assertIn(result, ['high', 'low'])

    def test_round_3_compares_against_two_previous_cards(self):
        self.game.game(1, 'red')
        self.game.game(2, 'high')
        result, card = self.game.game(3, 'between')
        self.assertIn(result, ['between', 'outside'])

    def test_round_4_returns_suit_result(self):
        self.game.game(1, 'red')
        self.game.game(2, 'high')
        self.game.game(3, 'between')
        result = self.game.game(4, 'Spades')
        self.assertIn(result, ['WINNNNNNEEEERRRRR', 'You lost'])

    def test_cards_are_stored_in_order(self):
        self.game.game(1, 'red')
        self.game.game(2, 'high')
        self.game.game(3, 'between')
        self.assertEqual(len(self.game.player.cards), 3)

