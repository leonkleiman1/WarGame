class Card:

    # get value and suit for card
    # value and suit for card
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

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
        pass
