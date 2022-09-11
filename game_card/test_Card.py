# Unit Test for Card Object
from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card_object = Card(2, 4)

    # get valid argument
    def test_init_valid(self):
        card = Card(1, 1)
        self.assertEqual(card.value, 1)
        self.assertEqual(card.suit, 1)
        card = Card(13, 4)
        self.assertEqual(card.value, 13)
        self.assertEqual(card.suit, 4)

    # get invalid value argument
    def test_init_invalid_value(self):
        # check the value
        with self.assertRaises(ValueError):
            card = Card(0, 4)
        with self.assertRaises(ValueError):
            card = Card(-1, 4)
        with self.assertRaises(ValueError):
            card = Card(14, 4)
        # check the suit
        with self.assertRaises(ValueError):
            card = Card(1, 0)
        with self.assertRaises(ValueError):
            card = Card(1, -1)
        with self.assertRaises(ValueError):
            card = Card(1, 5)

    # get invalid type
    def test_init_invalid_type(self):
        # check value
        with self.assertRaises(TypeError):
            card = Card(1.1, 4)
        with self.assertRaises(TypeError):
            card = Card("1", 4)
        # check suit
        with self.assertRaises(TypeError):
            card = Card(1, [4])
        with self.assertRaises(TypeError):
            card = Card(1, "4")

    # check if value of card equal than value of other card
    def test_eq_valid_true(self):
        card_value_eq = Card(2, 4)
        self.assertTrue(self.card_object == card_value_eq)

    # check if value of card not equal than value of other card
    def test_eq_valid_false(self):
        # the values in this case is different
        card_value_not_eq = Card(1, 4)
        self.assertFalse(self.card_object == card_value_not_eq)
        # the value in this case is equal, and suit is different
        card_value_not_eq = Card(2, 3)
        self.assertFalse(self.card_object == card_value_not_eq)

    # check if the type is not card
    def test_eq_invalid_type(self):
        with self.assertRaises(TypeError):
            if self.card_object == 1:
                pass

    # check if value of card is ace
    def test_gt_ace_value(self):
        card_with_ace = Card(1, 4)
        self.assertTrue(card_with_ace > self.card_object)
        self.assertFalse(self.card_object > card_with_ace)

    # check if value of card greater than value of other card
    def test_gt_valid(self):
        card_gt = Card(3, 4)
        self.assertTrue(card_gt > self.card_object)
        self.assertFalse(self.card_object > card_gt)

    # check if value of card equal than value of other card
    def test_gt_eq_value(self):
        card_eq_value = Card(2, 3)
        self.assertTrue(self.card_object > card_eq_value)
        self.assertFalse(card_eq_value > self.card_object)

    # check if the type is not card
    def test_gt_invalid_type(self):
        with self.assertRaises(TypeError):
            if self.card_object > 1:
                pass

    # check the card print
    def test_str(self):
        card = Card(1, 1)
        self.assertEqual("ace of Diamond", str(card))
        card = Card(2, 2)
        self.assertEqual("2 of Spade", str(card))
        card = Card(11, 3)
        self.assertEqual("jack of Heart", str(card))
        card = Card(12, 4)
        self.assertEqual("queen of Club", str(card))
        card = Card(13, 1)
        self.assertEqual("king of Diamond", str(card))

    # check the card print in list/dic/tup and more
    def test_repr(self):
        card = Card(1, 1)
        list_card = [card]
        self.assertEqual("[ |ace:Diamond| ]", str(list_card))
        card = Card(2, 2)
        list_card = [card]
        self.assertEqual("[ |2:Spade| ]", str(list_card))
        card = Card(11, 3)
        list_card = [card]
        self.assertEqual("[ |jack:Heart| ]", str(list_card))
        card = Card(12, 4)
        list_card = [card]
        self.assertEqual("[ |queen:Club| ]", str(list_card))
        card = Card(13, 1)
        list_card = [card]
        self.assertEqual("[ |king:Diamond| ]", str(list_card))
