import random

class Deck:
    def __init__(self):
        self.rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.cards = []
        for suit in self.suit:
            for rank in self.rank:
                self.cards.append(rank + ' of ' + suit)
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            return None
        card = self.cards.pop()
        rank, suit = self.get_suit_rank(card)
        return {
            'rank': rank,
            'suit': suit,
            'value': self.get_value(rank),
            'display': card
        }
    

    def get_suit_rank(self, card):
        suit_rank = card.split(" of ")
        return suit_rank[0], suit_rank[1]
    
    def get_value(self, rank):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return values.get(rank, 0)

    