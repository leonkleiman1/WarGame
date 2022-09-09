# Unit Test for CardGame Object
from unittest import TestCase
from unittest.mock import patch
from CardGame import CardGame  # Card Game Object
from DeckOfCards import DeckOfCards  # Deck if cards Object


class TestCardGame(TestCase):
    def setUp(self):
        self.manager_game_15 = CardGame("Oriel", "Leon", 15)  # creates CardGame with 15 cards to each of player

    # check valid argument in init function
    def test_init_valid(self):
        # check 10
        with patch('CardGame.CardGame.new_game') as mock_new_game:
            manager_game = CardGame("!@#name", "$%^name", 10)
            self.assertEqual(manager_game.p1.name, "!@#name")
            self.assertEqual(manager_game.p2.name, "$%^name")
            self.assertEqual(manager_game.p1.num, 10)
            self.assertEqual(type(manager_game.deck), DeckOfCards)
            mock_new_game.assert_called()
        # check 25
        with patch('CardGame.CardGame.new_game') as mock_new_game:
            manager_game = CardGame("!@#name", "$%^name", 25)
            self.assertEqual(manager_game.p1.name, "!@#name")
            self.assertEqual(manager_game.p2.name, "$%^name")
            self.assertEqual(manager_game.p1.num, 25)
            self.assertEqual(type(manager_game.deck), DeckOfCards)
            mock_new_game.assert_called()
        # check default
        with patch('CardGame.CardGame.new_game') as mock_new_game:
            manager_game = CardGame("!@#name", "$%^name")
            self.assertEqual(manager_game.p1.name, "!@#name")
            self.assertEqual(manager_game.p2.name, "$%^name")
            self.assertEqual(manager_game.p1.num, 26)
            self.assertEqual(type(manager_game.deck), DeckOfCards)
            mock_new_game.assert_called()

    # check invalid value argument in init function
    def test_init_invalid_value(self):
        # check number below 10
        with patch('CardGame.CardGame.new_game') as mock_new_game:
            manager_game = CardGame("oriel", "leon", 9)
            self.assertEqual(manager_game.p1.name, "oriel")
            self.assertEqual(manager_game.p2.name, "leon")
            self.assertEqual(manager_game.p1.num, 26)
            self.assertEqual(type(manager_game.deck), DeckOfCards)
            mock_new_game.assert_called()
        # check negative number
        with patch('CardGame.CardGame.new_game') as mock_new_game:
            manager_game = CardGame("oriel", "leon", -1)
            self.assertEqual(manager_game.p1.name, "oriel")
            self.assertEqual(manager_game.p2.name, "leon")
            self.assertEqual(manager_game.p1.num, 26)
            self.assertEqual(type(manager_game.deck), DeckOfCards)
            mock_new_game.assert_called()
        # check number above 26
        with patch('CardGame.CardGame.new_game') as mock_new_game:
            manager_game = CardGame("oriel", "leon", 27)
            self.assertEqual(manager_game.p1.name, "oriel")
            self.assertEqual(manager_game.p2.name, "leon")
            self.assertEqual(manager_game.p1.num, 26)
            self.assertEqual(type(manager_game.deck), DeckOfCards)
            mock_new_game.assert_called()

    # check if call to new_game, after create CardGame, raise Error
    def test_init_invalid_new_game(self):
        with self.assertRaises(ModuleNotFoundError):
            self.manager_game_15.new_game()

    def test_new_game(self):
        pass

    # check if equal return None
    def test_get_winner_valid_equal(self):
        self.assertEqual(self.manager_game_15.get_winner(), None)

    # check if p1 or p2 win
    def test_get_winner_valid_win(self):
        # append 1 more card to list of player 1 from deck
        manager_game = CardGame("oriel", "leon", 10)
        manager_game.p1.add_card(manager_game.deck.deal_one())
        self.assertEqual(manager_game.get_winner(), manager_game.p1)
        # append 2 more card to list of player 2 from deck
        manager_game.p2.add_card(manager_game.deck.deal_one())
        manager_game.p2.add_card(manager_game.deck.deal_one())
        self.assertEqual(manager_game.get_winner(), manager_game.p2)
