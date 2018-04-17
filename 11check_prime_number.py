"""
Ask the user for a number and determine whether the number is prime or not.
"""

num = int(input("Enter a number to check if it is prime.\n> "))

for div in range(2,num-1):
    check = num % div

    if check == 0:
        print("Not prime")
    else:
        print("Your number ({}) is prime!".format(num))
    break

    
