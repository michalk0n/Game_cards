from Cardgame_class import CardGame
from time import sleep

def main():

    name1 = str(input("Enter your name: "))
    name2 = str(input("Enter your name: "))
    players = CardGame(name1, name2) # starting a game with 26 cards for each player
    player1 = players.player1
    player2 = players.player2
    print(f"{player1} \n{player2}")

    print("--Game start in 3 sec--")
    sleep(3)
    for i in range(10):
        print(f"--Round {i+1}:")
        sleep(2)
        card1 = player1.get_card()
        card2 = player2.get_card()

        print(f"{player1.player_name}'s card: {card1}\n"
            f"{player2.player_name}'s card: {card2}")
        if card1 > card2:
            player1.add_card(card1)
            player1.add_card(card2)
            winner = player1

        elif card2 > card1:
            player2.add_card(card1)
            player2.add_card(card2)
            winner = player2

        else:
            player1.add_card(card1)
            player2.add_card(card2)
            winner = None

        print(f"this round winner is: {winner.player_name}")
    sleep(3)
    print(f"the winner of the game is {players.get_winner().player_name} 🏆🥳")

main()
