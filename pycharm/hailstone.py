"""
File: hailstone.py
Name:馮令彝
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print('This program computes Hailstone sequence')
    a = int(input("Enter a number: "))
    b = 0
    while not a == 1:
        if a % 2 == 1:
            print(str(a) + " is odd so I make 3n+1: " + str(a * 3 + 1))
            a = a * 3 + 1
            b = b+1
        else:
            print(str(a) + " is even so I take half: " + str(a // 2))
            a = a // 2
            b = b+1
    print('It takes ' + str(b) +' steps to raech 1')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
