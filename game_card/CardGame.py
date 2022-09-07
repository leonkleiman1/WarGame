# Card Game Object
from Player import Player
from DeckOfCards import DeckOfCards


class CardGame:
    """holds information about the deck """

    def __init__(self, _name_p1, _name_p2, _num_per_player=26):
        # check if num_per_player between 10-26, if not change to 26
        if _num_per_player < 10 or _num_per_player > 26:
            _num_per_player = 26

        self.is_start = False  # hold boolean value if the game start

        self.p1 = Player(_name_p1, _num_per_player)
        self.p2 = Player(_name_p2, _num_per_player)
        self.deck = DeckOfCards()
        self.new_game()
        self.is_start = True

    # start new game: shuffle the deck and gives cards to players
    def new_game(self):
        if self.is_start:
            raise ValueError("The function cannot be called outside the init!!!")
        self.deck.card_shuffle()
        self.p1.set_hand(self.deck)
        self.p2.set_hand(self.deck)

    # return the player with the most cards in the hand, if is equal return None
    def get_winner(self):
        if len(self.p1.list_cards) == len(self.p2.list_cards):
            return
        elif len(self.p1.list_cards) > len(self.p2.list_cards):
            return self.p1
        return self.p2
