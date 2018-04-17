"""
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean.

Extras:

    Use binary search.
"""

import random

def generate_ordered_list(length):
    order_list = []
    for i in range(length):
        order_list.append(random.randint(0,20))
    order_list.sort()
    return order_list

def element_search(a_list, num):
    print(a_list)
    print(num)
    if num in a_list:
        print("Your number is in the list.")
    else:
        print("Your number is not in the list.")

element_search(generate_ordered_list(10),random.randint(0,20))
    
