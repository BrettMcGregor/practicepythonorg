"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating a
new password every time the user asks for a new password. Include your
run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords,
    pick a word or two from a list.

"""
from string import ascii_letters, digits
from string import printable
from random import choice

def password_gen():
    length = int(input("Enter a password length.\n> "))
    strength = input("Enter a password strength. 'weak' or 'strong'.\n> ")
    password = []
    if strength == "strong":
        for i in range(length):
            password.append(choice(printable))
    elif strength == "weak":
        for i in range(length):
            password.append(choice(ascii_letters+digits))
    else:
        print("error. Try again.")
        password_gen()
    print("Here is your password:\n"+"".join(password))

password_gen()
