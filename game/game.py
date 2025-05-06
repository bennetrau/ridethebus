from game.deck import Deck
from game.player import Player

class RideTheBus:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()

    def game(self, round, guess):
        card = self.deck.draw()
        self.player.add_card(card)

        #Black ro Red
        if round == 1:
            if (card['suit'] == 'Hearts' or card['suit'] == 'Diamonds'):
                color = 'red'
            else:
                color = 'black'
            return color, card
        #High or Lower
        elif round == 2:
            prev_card = self.player.cards[0]
            if card['value'] < prev_card['value']:
                result =  'low'
            else:
                result = 'high'
            return result, card
        
        #Between or out
        elif round == 3:
            first_card = self.player.cards[0]
            second_card = self.player.cards[1]
            low = min(first_card['value'], second_card['value'])
            high = max(first_card['value'], second_card['value'])
            if low <= card['value'] <= high:
                result = 'between'
            else:
                result = 'outside'
            return result, card
        
        #suit guess
        elif round == 4:
            if guess == card['suit']:
                result = 'WINNNNNNEEEERRRRR'
            else:
                result = 'You lost'
            return result
        
        return False, card
            