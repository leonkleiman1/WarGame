class Card:

    # get value and suit for card
    # value and suit for card
    def __init__(self, _value, _suit):
        if _suit > 4 or _suit < 1:
            raise ValueError("suit must be between 1-4")

        self.value = _value
        self.suit = _suit

    # check if value of card1 equal to value of card2
    def __eq__(self, card2):
        if self.value == card2.value:
            return True
        else:
            return False

    def __gt__(self, card2):
        # check if card is ace
        if self.value == 1 and card2.value != 1:
            return True
        if card2.value == 1 and self.value != 1:
            return False
        # check value of card
        if self.value > card2.value:
            return True
        elif self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False

    def __str__(self):
        #dict for card with special type
        dict_value = {1: "ace", 11: "jack", 12: "queen", 13: "king"}
        #dict for value of suit
        dict_suite = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        if 1 < self.value < 11:
            return f'Value: {self.value}, Suite:{dict_suite[self.suit]}'
        else:
            return f'Value: {dict_value[self.value]}, Suite: {dict_suite[self.suit]}'

    def __repr__(self):
        dict_value = {1: "ace", 11: "jack", 12: "queen", 13: "king"}
        dict_suite = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        if 1 < self.value < 11:
            return f'{self.value},  {dict_suite[self.suit]}'
        else:
            return f'{dict_value[self.value]},  {dict_suite[self.suit]}'
