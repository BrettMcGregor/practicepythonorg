"""

Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)

"""

def is_palindrome(string):
    if string[-1::-1] == string:
        print("You have a palindrome")
    else:
        print("Not a palindrome")

is_palindrome("fartass")
