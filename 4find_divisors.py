"""
Create a program that asks the user for a number and then prints
out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides
evenly into another number. For example, 13 is a divisor of 26
because 26 / 13 has no remainder.)

Extra Credit (Bretts idea) repeat but factor the number for perfect squares

"""

#user input. check for int

num = input("Please enter a number. I will return the divisors for you.\n> ")

#find divisors of user input number

possible_divisors = list(range(1,int(num)+1))
print(possible_divisors)
divisors = []
for number in possible_divisors:
    if num % number == 0:
        divisors.append(number)

#print divisors of number
print(divisors)
