import unittest
import random
from unittest.mock import MagicMock

### PRODUCTION CODE ##########

class BlackJack:
    deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

    def __init__(self, random):
        self.random = random

    def give_a_card(self):
        card = self.random.choice(self.deck)
        self.deck.remove(card)
        return card
    

#################################


class TestTheBlackJack(unittest.TestCase):
    
    def setUp(self):
        self.my_random = MagicMock()        
        self.blackjack = BlackJack(self.my_random)
        
    def test_when_card_is_given_is_eliminated_from_desk(self):
        self.my_random.choice.return_value = 4

        self.blackjack.give_a_card()

        assert len(self.blackjack.deck) == 43
        assert self.blackjack.deck.count(4) == 3
        self.my_random.choice.assert_called_with(self.blackjack.deck)

    