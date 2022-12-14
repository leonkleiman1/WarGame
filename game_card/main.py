# War game
# Main file of project
from CardGame import CardGame

# create 2 players for the game
name_p1 = input("Enter name of player 1: ")
name_p2 = input("Enter name of player 2: ")
# input again if the names are empty
while len(name_p1.split()) == 0:
    print("Name of player 1 is empty!")
    name_p1 = input("Enter name of player 1 again: ")
while len(name_p2.split()) == 0:
    print("Name of player 2 is empty!")
    name_p2 = input("Enter name of player 2 again: ")
# input again if the names are same
while name_p1 == name_p2:
    print("The names are same!")
    name_p2 = input("Enter name of player 2 again: ")

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
        print(f"# The winner in this round is: {name_p1} #")
    else:
        manager_game.p2.add_card(card_p2)
        manager_game.p2.add_card(card_p1)
        print(f"# The winner in this round is: {name_p2} #")


# print the winner of the game, or if we have None print tie
print("===The End===")
if manager_game.get_winner() is None:
    print("The result is Tie")
else:
    print(f"The winner of the game is...")
    print(manager_game.get_winner())
