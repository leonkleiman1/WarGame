# Unit Test for Player Object
from unittest import TestCase, mock
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player_dan_15 = Player("Dan", 15)
        self.deck_object = DeckOfCards()  # deck of cards for tests

    # check the valid arguments. the num argument need to be between 10-26
    def test_init_valid(self):
        player = Player("name_#@.", 10)  # check 10
        self.assertEqual(player.name, "name_#@.")
        self.assertEqual(player.num, 10)
        self.assertEqual(player.cards_player, [])
        player = Player("name_#@. ", 25)  # check 25
        self.assertEqual(player.name, "name_#@. ")
        self.assertEqual(player.num, 25)
        self.assertEqual(player.cards_player, [])
        player = Player("_#$%Name")  # check default
        self.assertEqual(player.name, "_#$%Name")
        self.assertEqual(player.num, 26)
        self.assertEqual(player.cards_player, [])

    # check invalid value num
    def test_init_invalid_value(self):
        player = Player("Name", 9)  # check 9
        self.assertEqual(player.num, 26)
        self.assertEqual(player.cards_player, [])
        player = Player("Name", -1)  # check negative number
        self.assertEqual(player.num, 26)
        self.assertEqual(player.cards_player, [])
        player = Player("Name", 27) # check 27
        self.assertEqual(player.num, 26)
        self.assertEqual(player.cards_player, [])

    # check the type of arguments
    def test_init_invalid_type(self):
        # check num
        with self.assertRaises(TypeError):
            player = Player("Name", 10.1)
        with self.assertRaises(TypeError):
            player = Player("Name", "25")
        # check name
        with self.assertRaises(TypeError):
            player = Player(["Name"], 0)
        with self.assertRaises(TypeError):
            player = Player(123, 0)

    # check if the cards_player in the correct length,
    # and the card from deal_one in the list
    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(1, 4))
    def test_set_hand_valid(self, mock_deal_one):
        self.player_dan_15.set_hand(self.deck_object)
        self.assertEqual(len(self.player_dan_15.cards_player), 15)
        self.assertIn(Card(1, 4), self.player_dan_15.cards_player)
        # check default num_per_player
        player = Player("name")
        player.set_hand(self.deck_object)
        self.assertEqual(len(player.cards_player), 26)
        self.assertIn(Card(1, 4), player.cards_player)

    # check invalid deck
    def test_set_hand_invalid(self):
        with self.assertRaises(TypeError):
            self.player_dan_15.set_hand([])
        with self.assertRaises(TypeError):
            self.player_dan_15.set_hand(12)

    # check the function get_card work
    def test_get_card_valid(self):
        self.player_dan_15.add_card(Card(1, 4))
        self.player_dan_15.add_card(Card(2, 4))
        self.assertTrue(len(self.player_dan_15.cards_player) == 2)
        self.assertEqual(Card(1, 4), self.player_dan_15.get_card())
        self.assertTrue(len(self.player_dan_15.cards_player) == 1)

    # check if the length of cards_player is 0
    def test_get_card_invalid_length(self):
        with self.assertRaises(IndexError):
            self.player_dan_15.get_card()

    # check the function add_card work
    def test_add_card_valid(self):
        self.player_dan_15.add_card(Card(1, 4))
        self.assertTrue(len(self.player_dan_15.cards_player) == 1)
        self.assertIn(Card(1, 4), self.player_dan_15.cards_player)

    # check the type of deck
    def test_add_card_invalid_type(self):
        with self.assertRaises(TypeError):
            self.player_dan_15.add_card(1)
        with self.assertRaises(TypeError):
            self.player_dan_15.add_card("Card")

    # check if the method get same card in the list
    def test_add_card_same_card(self):
        self.player_dan_15.add_card(Card(1, 4))
        with self.assertRaises(ValueError):
            self.player_dan_15.add_card(Card(1, 4))

    # check if the method add card to the list with length 52
    def test_add_card_above_52_cards(self):
        self.assertTrue(len(self.deck_object.deck) == 52)
        # fill in hand of player 52 cards
        for card in self.deck_object.deck:
            self.player_dan_15.add_card(card)
        self.assertTrue(len(self.player_dan_15.cards_player) == 52)
        # add card (not exist in the list) to cards of player
        with self.assertRaises(ValueError):
            self.player_dan_15.add_card(Card(1, 5))
        # add card (exist in the list) to cards of player
        with self.assertRaises(ValueError):
            self.player_dan_15.add_card(Card(1, 4))

