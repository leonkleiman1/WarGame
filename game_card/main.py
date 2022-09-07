# War game
# Main file of project
from CardGame import CardGame

# create 2 players for the game
name_p1 = input("Enter name of player 1: ")
name_p2 = input("Enter name of player 2: ")
manager_game = CardGame(name_p1, name_p2)

# print the players
print(manager_game.p1)
print(manager_game.p2)

# do 10 rounds
for i in range(10):
    print(f'===Round {i+1}===')
    card_p1 = manager_game.p1.get_card()
    card_p2 = manager_game.p2.get_card()
    print(f"{name_p1}'s Card: {card_p1}")
    print(f"{name_p2}'s Card: {card_p2}")

    # check which player have the greater card
    if card_p1 > card_p2:
        manager_game.p1.add_card(card_p1)
        manager_game.p1.add_card(card_p2)
    else:
        manager_game.p2.add_card(card_p2)
        manager_game.p2.add_card(card_p1)
    # print the winner in this round or tie
    if manager_game.get_winner() is None:
        print("-Tie-")
    else:
        print(f"# The winner in this round is: {manager_game.get_winner().name} #")

# print the winner of the game, or if we have tie print tie
print("===The End===")
if manager_game.get_winner() is None:
    print("The result is Tie")
else:
    print(f"The winner of the game is...")
    print(manager_game.get_winner())


