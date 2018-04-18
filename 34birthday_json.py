"""
This exercise is Part 1 of 4 of the birthday data exercise series. 

For this exercise, we will keep track of when our friend’s birthdays are, and be able to
find that information based on their name. Create a dictionary (in your file) of names and
birthdays. When you run your program it should ask the user to enter a name, and return
the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.

Happy coding!
"""

birthdays = {"Brett": "21/04/1976", "Andrea": "27/03/1975", "Devon":"15/07/2010",
             "Ryan":"02/07/2013"}
keys = birthdays.keys()

for key in keys:
    print(key)
selection = input("Enter a name to find out that persons birthday.\n")

print(birthdays[selection])

