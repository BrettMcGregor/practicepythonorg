"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number
    and printing out that many copies of the previous message. (Hint:
    order of operations exists in Python)
    Print out that many copies of the previous message on separate lines.
    (Hint: the string "\n is the same as pressing the ENTER button)

"""
def year100():
    name = input("Enter your name: ")
    age = int(input("Enter your age?: "))
    repeat = int(input("How many times do you need to hear this? "))
    current_year = 2018
    year_100 = current_year-age+100
    print("{}, you will turn 100 in the year {}\n".format(name,year_100)*repeat)

year100()
    
