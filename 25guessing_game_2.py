"""

In a previous exercise, we’ve written a program that “knows” a number and asks a
user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in
your head a number between 0 and 100. The program will guess a number, and you,
the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it
took to get your number.

As the writer of this program, you will have to choose how your program will
strategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an
optimal guessing strategy. An alternate strategy might be to guess 50
(right in the middle of the range), and then increase / decrease by 1 as needed.
After you’ve written the program, try to find the optimal strategy! (We’ll talk
about what is the optimal one next week with the solution.)

"""
import random

#in a loop
    #computer guesses number between 0 and 100
    #user provides feedback, high, low or correct
    #track number of guesses
    #keep a list of guesses made
    #handle user input exceptions

def guess():
    guesses = []
    lower = 0
    upper = 100
    attempts = 0
    while True:
        attempts += 1
        new_guess = int((lower+upper)/2)
        guesses.append(new_guess)
        print("Computer guesses:",guesses)
        user_feedback = input("How was my guess? High(h), Low(l), Correct(c)\n> ")
        if user_feedback.lower() == "h":
            upper = new_guess
        elif user_feedback.lower() == "l":
            lower = new_guess
        elif user_feedback.lower() == "c":
            print("Great!!! I guessed your number. It was {}.\nIt took me {} guesses."
                  .format(new_guess,attempts))
            break
        else:
            print("I did not understand that. Try again.")
            attempts -= 1
            del guesses[-1]
            continue
        
def new_game():
    while True:
        start = input("\nOK. You want me to guess your number between 0 and 100? (Y/n)\n>  ")
        if start.upper() == "N":
            print("OK. See you next time.")
            break
        elif start.upper() == "Y":
            guess()
        else:
            print("Sorry I didnt understand that.")
                
new_game()
