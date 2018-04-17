"""
As you may have guessed, we are trying to build up to a full tic-tac-toe board. However,
this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space,
and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is
3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO
people have won - assume that in every board there will only be one winner.
"""


#check tic tac toe grid for complete rows containing users token 3 horizontal,
#3 vertical and 2 diagonal. Report if no winner
game = [[1, 1, 0],
	[2, 1, 0],
	[1, 2, 1]]

win = False

#check rows and columns
for i in range(1,3):
    for x in range(0,3):
        if game[x][0] == i and game[x][1] == i and game[x][2] == i:
            print("win row {}, player {}".format(x+1,i))
            win = True
        if game[0][x] == i and game[1][x] == i and game[2][x] == i:
            print("win column {}, player {}".format(x+1,i))
            win = True
        x += 1
    i += 1

#check diagonals
for i in range(1,3):
    if game[0][0] == i and game[1][1] == i and game[2][2] == i:
        print("win diagonal 1, player {}.".format(i))
        win = True
    if game[2][0] == i and game[1][1] == i and game[0][2] == i:
        print("win diagonal 2, player {}.".format(i))
        win = True
    i += 1

if win != True:
    print("No winner.")

