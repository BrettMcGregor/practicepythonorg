"""
This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises
are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word
from a list of words from the SOWPODS dictionary. Download this file and save
it in the same directory as your Python code.

"""

import random

with open("sowpods.txt", "r") as f:
    line = f.readline()
    while line:
        line = f.readline()

print("The entire file has been read!")
