"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / oddnumber react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.

    Ask the user for two numbers: one number to check (call it num) and one
    number to divide by (check).

    If check divides evenly into num, tell that to the user. If not, print a
    different appropriate message.
"""

def odd_even():
    try:
        num = int(input("Enter a number:\n> "))
        check = int(input("Enter a divisor:\n> "))
        if num % check == 0:
            print("{} is a multiple of {}.".format(num,check))
        if num % 4 == 0:
            print("Your number is a multiple of four.")
        if num % 2 == 0:
            print("Your number is even.")
        else:
            print("Your number is odd.")
        replay()
    except ValueError:
        print("Please enter a positive integer only")
        replay()
   

def replay():
    replay = str(input("Do you want to try again? Y/n\n> "))

    if replay.lower() == "n":
        print("OK. See you next time.")
        exit
    else:
        if replay.upper() == "Y":
            odd_even()

odd_even()
