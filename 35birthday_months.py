"""
In the previous exercise we saved information about famous scientists’ names
and birthdays to disk. In this exercise, load that JSON file from disk, extract
the months of all the birthdays, and count how many scientists have a birthday
in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""
import json
from collections import Counter

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

keys = birthdays.keys()
values = birthdays.values()

month_dict = {"01":"January",
              "02":"February",
              "03":"March",
              "04":"April",
              "05":"May",
              "06":"June",
              "07":"July",
              "08":"August",
              "09":"September",
              "10":"October",
              "11":"November",
              "12":"December"}

birthdates = []
months = []
count = []

for key in keys:
    birthdates.append(birthdays[key])

for item in birthdates:
    months.append(item.split("/"))

for i in range(0, len(birthdates)):
        del months[i][0]
        del months[i][1]

for item in months:
    count.append(item[0])

c = Counter(count)
c = dict(c)

print("\nNumber of birthday occurences in each month:\n")
for month in c:
    print(month_dict[month],c[month])
print("\n"*2)
print("Known birthdays:\n")
for key in keys:
    print(key)
    
selection = input("\nEnter a name to find out that persons birthday.\n> ")

print(birthdays[selection])

new_key = input("Enter a name to add to the birthday dictionary:")
new_value = input("Enter a birthday to add to the birthday dictionary:")

birthdays.update({new_key: new_value})

with open("birthdays.json", "w") as f:
    json.dump(birthdays, f)
