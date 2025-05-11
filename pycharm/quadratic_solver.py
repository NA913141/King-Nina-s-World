"""
File: quadratic_solver.py
Name:馮令彝
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print('Quadratic Solver')
	a = float(input('a:'))
	b = float(input('b:'))
	c = float(input('c:'))
	d = b*b-4*a*c
	e = math.sqrt(d)
	f = (-b+e)/2/a
	g = (-b - e) / 2 / a
	if d > 0:
		print("Two roots: " + str(f, g))
	elif d == 0:
		print("One root: " + str(f))
	else:
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
