from game_card.CardGame import CardGame

# create the players
name_player1 = input("Enter name for player 1: ")
name_player2 = input("Enter name for player 2: ")
num_cards_per_player = int(input("How many cards you want for each player: "))
manager_game = CardGame(name_player1, name_player2, num_cards_per_player)

# do 10 rounds in war game
for i in range(10):
    print(f'===Round {i + 1}===')
    use_card_p1 = manager_game.p1.get_card()  # get card from player 1
    use_card_p2 = manager_game.p2.get_card()  # get card from player 2
    print(f'Card of {name_player1}: {use_card_p1}')
    print(f'Card of {name_player2}: {use_card_p2}')
    # check the winner in this round
    if use_card_p1 > use_card_p2:
        manager_game.p1.get_card(use_card_p1)
        manager_game.p1.get_card(use_card_p2)
        print(f"The winner in this round is {name_player1}")
    elif use_card_p2 > use_card_p1:
        manager_game.p2.get_card(use_card_p1)
        manager_game.p2.get_card(use_card_p2)
        print(f"The winner in this round is {name_player2}")
    elif use_card_p2 == use_card_p1:
        manager_game.p1.get_card(use_card_p1)
        manager_game.p2.get_card(use_card_p2)
        print(f"-Tie-")

# print the winner in the game after 10 rounds
print(manager_game.get_winner())
