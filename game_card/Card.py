# Card Object
class Card:
    """hold information of the card, value and suit"""

    # create card with value and suit for card
    def __init__(self, _value, _suit):
        # check if the type of value or suit not int
        if type(_value) != int or type(_suit) != int:
            raise TypeError("The type of argument is wrong!!!")
        # check if suite between 1-4
        if _suit > 4 or _suit < 1:
            raise ValueError("the argument must be between 1-4!!!")
        # check if value between 1-13
        if _value > 13 or _value < 1:
            raise ValueError("the argument must be between 1-4!!!")

        self.value = _value
        self.suit = _suit

    # check if value of this card equal to value of card2
    def __eq__(self, card2):
        # check the type
        if type(card2) != Card:
            raise TypeError("The argument is not Card!!!")
        if self.value == card2.value and self.suit == card2.suit:
            return True
        else:
            return False

    # check which card is greater, if the value equal, according to the suit
    def __gt__(self, card2):
        # check the type
        if type(card2) != Card:
            raise TypeError("The argument is not Card!!!")
        # check if card is ace
        if self.value == 1 and card2.value != 1:
            return True
        if card2.value == 1 and self.value != 1:
            return False
        # check value of card greater
        if self.value > card2.value:
            return True
        elif self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False

    # return the information of card
    def __str__(self):
        # dictionary for card with special type
        dict_value = {1: "ace", 11: "jack", 12: "queen", 13: "king"}
        # dictionary for value of suit
        dict_suite = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        if 1 < self.value < 11:
            return f'{self.value} of {dict_suite[self.suit]}'
        else:
            return f'{dict_value[self.value]} of {dict_suite[self.suit]}'

    # return the information of card
    def __repr__(self):
        dict_value = {1: "ace", 11: "jack", 12: "queen", 13: "king"}
        dict_suite = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        if 1 < self.value < 11:
            return f' |{self.value}:{dict_suite[self.suit]}| '
        else:
            return f' |{dict_value[self.value]}:{dict_suite[self.suit]}| '
