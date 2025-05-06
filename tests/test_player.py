import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_starts_with_empty_hand(self):
        player = Player()
        self.assertEqual(player.cards, [])

    def test_add_card_adds_one_card(self):
        player = Player()
        card = {'rank': 'A', 'suit': 'Spades', 'value': 14}
        player.add_card(card)
        self.assertIn(card, player.cards)

    def test_add_card_increases_card_count(self):
        player = Player()
        player.add_card({'rank': '2', 'suit': 'Hearts', 'value': 2})
        player.add_card({'rank': 'K', 'suit': 'Clubs', 'value': 13})
        self.assertEqual(len(player.cards), 2)
