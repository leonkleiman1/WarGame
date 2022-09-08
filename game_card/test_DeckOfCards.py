from unittest import TestCase
from DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck = DeckOfCards()


    #check if deck with 52 cards
    def test_init_valid(self):
        self.assertEqual(len(self.deck.deck), 52)
    #check if crads are not duplicate
        emp_list = []
        for card in self.deck.deck:
            if card not in emp_list:
                emp_list.append(card)
        self.assertTrue(len(emp_list) == 52)

    #get suffeled deck
    def test_card_shuffle(self):
        not_shuffled_deck = self.deck.deck.copy()
        self.deck.card_shuffle()

        self.assertTrue(not_shuffled_deck != self.deck.deck)

    #deal one card
    def test_deal_one(self):
        card=self.deck.deal_one()
        #check the len of deck after deal one card
        self.assertEqual(len(self.deck.deck), 51)
        #check if the dealed card not exist in the deck
        self.assertNotIn(card,self.deck.deck)
    #deal all cards of deck
    def test_deal_one_empty_deck(self):
        for i in range(52):
            self.deck.deal_one()
        self.assertEqual(len(self.deck.deck),0)

        self.assertEqual(self.deck.deal_one(),None)











