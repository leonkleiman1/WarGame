# Deck of cards Object
from Card import Card
import random


class DeckOfCards:
    """object that create a deck of cards and is able to perform actions on it"""

    def __init__(self):
        self.deck = []  # empty deck of cards
        # create a deck
        for value in range(1, 14):
            for suite in range(1, 5):
                new_card = Card(value, suite)
                self.deck.append(new_card)

    # the function shuffle the deck
    def card_shuffle(self):
        random.shuffle(self.deck)

    # the function return random card from the deck and remove it
    def deal_one(self):
        if len(self.deck) == 0:
            return
        card_return = self.deck[random.randint(1, len(self.deck))]
        self.deck.remove(card_return)
        return card_return
