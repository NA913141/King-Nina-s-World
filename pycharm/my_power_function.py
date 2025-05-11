"""
File: my_power_function.py
Name: 馮令彝
-------------------------------
This program shows students how to 
make their own functions by defining
def my_power(a, b)
"""


def my_add(n1, n2):
	return n1+n2


def my_sub(b, a):
	return b-a


def my_multi(n, m):
	return n*m


def main():
	a = int(input("a: "))
	b = int(input("b: "))
	ans = my_add(a, b)
	print(ans)

	ans = my_sub(a, b)
	print(ans)

	ans = my_multi(a, b)
	print(ans)

	print('This program prints a to the power of b.')
	print(my_power(a, b))


def my_power(a, b):
	ans = 1
	for i in range(b):
		ans = ans * a
	return ans


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
