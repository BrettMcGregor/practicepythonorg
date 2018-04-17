"""
Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter. The player
guesses one letter at a time until the entire word has been guessed. (In
the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep
track of the letters the player guessed and display a different message if
the player tries to guess that letter again. Remember to stop the game when
all the letters have been guessed correctly! Don’t worry about choosing a word
randomly or keeping track of the number of guesses the player has remaining -
we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...

And so on, until the player gets the word.

"""

def check_previous(guess, previous_guesses):
    if guess in previous_guesses:
        print("You have already guessed that letter! Try again.")
    else:
        previous_guesses.append(guess)

def check_letter(guess, word, correct_guesses, found):
    for letter in word:
        if guess == letter:
            found.append(guess)
            if guess not in correct_guesses:
                correct_guesses.append(letter)
    if guess not in word:
        print("Incorrect. Try again.")

def print_word(correct_guesses, word):
    for letter in word:
        if letter in correct_guesses:
            print(letter, end = "")
        else:
            print("_ ", end = "")   
            
word = "evaporate"

#welcome message and prompt for user to guess a letter
print("Welcome to Hangman!")
previous_guesses = []
correct_guesses = []
found = []

while True:
    print_word(correct_guesses, word)
    guess = input("\nGuess a letter>  ")
    
    #keep track of previous letters guessed
    check_previous(guess, previous_guesses)
    
    #check if letter is in word
    check_letter(guess,word, correct_guesses, found)

    if len(found) == len(word):
        if len(previous_guesses)-len(correct_guesses) == 1:
            print("Congrats! You guessed the word. You had {} incorrect guess."
              .format(len(previous_guesses)-len(correct_guesses)))
            break
        else:
            print("Congrats! You guessed the word. You had {} incorrect guesses."
                  .format(len(previous_guesses)-len(correct_guesses)))
            break
    
print("Game over")


