"""
Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers in
the sequence to generate.

(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""


def fibonnaci():
    length = int(input("Generate a Fibonacci sequence. Enter how many numbers:\n>  "))
    fib_list = []
    
    if length <= 2:
        for i in range(length):
            fib_list.append(1)
    else:
        fib_list.append(1)
        fib_list.append(1)
        for i in range(length):
            fib_list.append(fib_list[-2] + fib_list[-1])

    for item in fib_list:
        print(item)

fibonnaci()
