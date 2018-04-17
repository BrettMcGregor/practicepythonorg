"""

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high,
or exactly right. (Hint: remember to use the user input lessons from the very firstexercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print
    this out.

"""

import random

def game():
    attempts = 0
    while True:    
        guess = input("\nEnter a number between 1 and 10\n> ")
        
        if guess.lower() == "exit":
            print("OK. See you next time.")
            break

        guess = int(guess)
        
        if guess == secret_num:
            attempts += 1
            print("You got it in {} attempts".format(attempts))
            break
        elif guess < secret_num:
            print("Too low")
            attempts += 1
        elif guess > secret_num:
            print("Too high")
            attempts += 1
        else:
            print("Error. Try again.")
            break

secret_num = random.randint(1,9)

print("\n\nNumber Guessing Game\n"+"-"*20)
    
game()


