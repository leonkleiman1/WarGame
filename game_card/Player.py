from DeckOfCards import DeckOfCards
from Card import Card
class Player:

# a method that creat player
    def __init__(self, _name_player, _num_per_player=26):
        if _num_per_player < 10 or _num_per_player > 26:
            _num_per_player = 26

        self.name = _name_player
        self.cards_player = []
        self.num = _num_per_player


# method that creat a deck for player
    def set_hand(self,deck:DeckOfCards):
        for card in range(self.num):
            self.cards_player.append(deck.deal_one())


# method that get card from player deck
    def get_card(self):
        return self.cards_player.pop()


# method that add card to player deck
    def add_card(self,card:Card):
        self.cards_player.append(card)

    def __str__(self):
        return f"Player name:{self.name},\nPlayer's hand:{self.cards_player}"
