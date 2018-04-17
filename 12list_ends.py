"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.

For practice, write this code inside a function.
"""
import random

def autolist():
    alist = []
    length = 10
    for i in range(length):
        alist.append(random.randint(1,1000))

    new_list = []
    new_list.append(alist[0])
    new_list.append(alist[-1])
    print(alist)
    print(new_list)

autolist()

    
