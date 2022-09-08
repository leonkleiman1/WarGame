# Player object
from DeckOfCards import DeckOfCards
from Card import Card


class Player:
    """holds information about player"""

    # a method that create player
    def __init__(self, _name_player, _num_per_player=26):
        # check if type of name or type of num_per_player is correct
        if type(_name_player) != str or type(_num_per_player) != int:
            raise TypeError("The type of argument is wrong!!!")
        # check if num_per_player is between 10-26, else put 26
        if _num_per_player < 10 or _num_per_player > 26:
            _num_per_player = 26

        self.name = _name_player
        self.cards_player = []  # empty list cards of player
        self.num = _num_per_player

    # method that create a deck for player
    def set_hand(self, deck: DeckOfCards):
        # check the type if is DeckOfCards
        if type(deck) != DeckOfCards:
            raise TypeError("The deck must be type of DeckOfCards!!!")
        for card in range(self.num):
            self.cards_player.append(deck.deal_one())

    # method that get card from player deck from the index 0
    def get_card(self):
        card = self.cards_player[0]
        self.cards_player.remove(card)
        return card

    # method that add card to player deck
    def add_card(self, card: Card):
        # check if type of card is correct
        if type(card) != Card:
            raise TypeError("You can add only a card!!!")
        # check if you add same card
        for card_player in self.cards_player:
            if card_player == card:
                raise ValueError("The card exist in the list of cards!!!")
        self.cards_player.append(card)

    # return information about the player
    def __str__(self):
        return f"Player name:{self.name},\nPlayer's hand:{self.cards_player}"
