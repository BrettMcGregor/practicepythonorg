"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want
to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""
import sys

def game():
    print("Hi. This is two player Rock Paper Scissors game.\nEach player must choose either \
Rock(r), Paper(p), or Scissors(s)")
    player1 = input("Player One> ")
    print("\n"*80)
    player2 = input("Player Two> ")
    while True:
        if player1 == player2:
            print("Both players called the same!")
        elif player1 == "r" and player2 == "s":
            print("Player One wins! Rock beats Scissors!")
        elif player1 == "s" and player2 == "p":
            print("Player One wins! Scissors beats Paper!")
        elif player1 == "p" and player2 == "r":
            print("Player One wins! Paper beats Rock!")
        elif player1 == "s" and player2 == "r":
            print("Player Two wins! Rock beats Scissors!")
        elif player1 == "p" and player2 == "s":
            print("Player Two wins! Scissors beats Paper!")
        elif player1 == "r" and player2 == "p":
            print("Player Two wins! Paper beats Rock!")
        else:
            print("Error. Try again.")
            game()
        new_game()
        break    

def new_game():
    replay = input("Would you like another round? (Y/n) >  ")
    while True:
        if replay.upper() == "N":
                print("OK. See you next time")
                return False
        else:
            if replay.upper() == "Y":
                print("\n"*80)
                game()
game()
#new_game()
