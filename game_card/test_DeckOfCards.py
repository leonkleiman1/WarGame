# Unit Test for DeckOfCard Object
from unittest import TestCase
from DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck_object = DeckOfCards()  # creates an orderly deck

    # check if the deck with 52 cards and not with same cards
    def test_init(self):
        # check that the deck contains 52 cards
        self.assertEqual(len(self.deck_object.deck), 52)
        # check if the cards are not duplicate
        emp_list = []
        for card in self.deck_object.deck:
            if card not in emp_list:
                emp_list.append(card)
        self.assertTrue(len(emp_list) == 52)

    # check if the orderly deck, shuffled
    def test_card_shuffle(self):
        not_shuffled_deck = self.deck_object.deck.copy()
        self.deck_object.card_shuffle()
        self.assertTrue(not_shuffled_deck != self.deck_object.deck)

    # check the function deal_one
    def test_deal_one(self):
        card = self.deck_object.deal_one()
        # check the len of deck after deal one card
        self.assertEqual(len(self.deck_object.deck), 51)
        # check if the dealt card not exist in the deck
        self.assertNotIn(card, self.deck_object.deck)

    # deal all the cards from the deck
    def test_deal_one_empty_deck(self):
        # empty the deck
        for i in range(52):
            self.deck_object.deal_one()

        self.assertEqual(len(self.deck_object.deck), 0)  # check the length of the deck
        self.assertEqual(self.deck_object.deal_one(), None)  # check the function return None
