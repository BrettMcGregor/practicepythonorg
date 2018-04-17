"""
In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game
in Python:

    Draw the Tic Tac Toe game board
    Checking whether a game board has a winner
    Handle a player move from user input

The next step is to put all these three components together to make a two-player Tic Tac
Toe game! Your challenge in this exercise is to use the functions from those previous
exercises all together in the same program to make a two-player game that you can play
with a friend. There are a lot of choices you will have to make when completing this
exercise, so you can go as far or as little as you want with it.

Here are a few things to keep in mind:

    You should keep track of who won - if there is a winner, show a congratulatory
    message on the screen.
    If there are no more moves left, don’t ask for the next player’s move!

As a bonus, you can ask the players if they want to play again and keep a running tally
of who won more - Player 1 or Player 2.
Tips

reuse work that has already been done!
"""
#----------------------------------------------------------------------------
# Draw the user moves

#user input for move coordinates row/col Note that start counting indexes here from one
#rather than zero

def player_move(player):
    print("\nPlayer {} move:".format(player))
    while True:
        try:
            location = input("\nEnter row, column coordinates (r,c) >")
            if game[int(location[0])-1][int(location[-1])-1] != 0:
                print("That cell is already occupied")
                continue
            else:
                game[int(location[0])-1][int(location[-1])-1] = player
                break
        except IndexError:
            print("That cell is outside the grid")
        except ValueError:
            print("I did not understand that. Try again.")


#play()
#----------------------------------------------------------------------------
#draw board function can take user input as argument
def draw_board():
        print(" _" * 3)
        for i in range (1,4):
            print("|_" * 3+"|")
   

#----------------------------------------------------------------------------
#Check for winner


def check_winner():
    win = False

#check rows and columns

    for x in range(0,3):
        if game[x][0] == "X" and game[x][1] == "X" and game[x][2] == "X":
            print("win row {}, player {}".format(x+1,"X"))
            win = True
        if game[0][x] == "X" and game[1][x] == "X" and game[2][x] == "X":
            print("win column {}, player {}".format(x+1,"X"))
            win = True
        x += 1

    for x in range(0,3):
        if game[x][0] == "O" and game[x][1] == "O" and game[x][2] == "O":
            print("win row {}, player {}".format(x+1,"Y"))
            win = True
        if game[0][x] == "O" and game[1][x] == "O" and game[2][x] == "O":
            print("win column {}, player {}".format(x+1,"O"))
            win = True
        x += 1

    #check diagonals
    if game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X":
        print("win down diagonal, player {}.".format("X"))
        win = True
    if game[2][0] == "X" and game[1][1] == "X" and game[0][2] == "X":
        print("win up diagonal, player {}.".format("X"))
        win = True
    if game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O":
        print("win down diagonal, player {}.".format("Y"))
        win = True
    if game[2][0] == "O" and game[1][1] == "O" and game[0][2] == "O":
        print("win up diagonal, player {}.".format("O"))
        win = True
      

    if win != True:
        print("No winner.")

    if win == True:
        return True




game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

#game introduction text
print("Welcome to the Tic Tac Toe game!\n")
draw_board()

moves = 0

while True:
    player_move("X")
    moves += 1
    print(game[0],"\n",game[1],"\n",game[2])
    #draw_board(3,3)
    if check_winner() == True:
        break
    if moves == 9:
        print("No more moves available.")
        break
    player_move("O")
    moves += 1
    print(game[0],"\n",game[1],"\n",game[2])
    if check_winner() == True:
        break
    if moves == 9:
        print("No more moves available.")
        break    

print("Game over.")





