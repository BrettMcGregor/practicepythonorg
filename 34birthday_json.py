"""
In the previous exercise we created a dictionary of famous scientists’ birthdays.
In this exercise, modify your program from Part 1 to load the birthday dictionary from
a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
and update the JSON file you have on disk with the scientist’s name. If you run the program
multiple times and keep adding new names, your JSON file should keep getting bigger and
bigger.
"""

import json

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

keys = birthdays.keys()

for key in keys:
    print(key)
selection = input("Enter a name to find out that persons birthday.\n")

print(birthdays[selection])

new_key = input("Enter a name to add to the birthday dictionary:")
new_value = input("Enter a birthday to add to the birthday dictionary:")

birthdays.update({new_key: new_value})

with open("birthdays.json", "w") as f:
    json.dump(birthdays, f)
