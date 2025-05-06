# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: This script covers basic loop practice, 
              random number parity check, multiplication tables, 
              temperature conversion, and drawing functions
"""

# Function to demonstrate passing by value
def change_value(x):
    x += 1
    return x

# --- Main: change_value ---
x = 8
print("Before change_value, x =", x)
print("Function return:", change_value(x))
print("After change_value, x =", x)
# --- End of Main: change_value ---


# Function to demonstrate passing by reference (list in Python)
def change_list(input_list):
    for i in range(len(input_list)):
        input_list[i] += 10
    return input_list

# --- Main: change_list ---
x = [2, 4, 6, 8]
print("\nBefore change_list, x =", x)
print("Function return:", change_list(x))
print("After change_list, x =", x)
# --- End of Main: change_list ---


# Function with variable number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# --- Main: sum_all ---
print("\nSum of none:", sum_all())
print("Sum of 1:", sum_all(1))
print("Sum of 10:", sum_all(10))
print("Sum of 1, 2, 3, 4, 5:", sum_all(1, 2, 3, 4, 5))
# --- End of Main: sum_all ---


# Function to return quotient and remainder
def div_and_mod(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# --- Main: div_and_mod ---
a, b = div_and_mod(100, 7)
print("\n100 divided by 7, quotient is", a, ", remainder is", b)
# --- End of Main: div_and_mod ---


# Function to compute sum and absolute difference
def sum_and_diff(num1, num2):
    sum_result = num1 + num2
    diff_result = abs(num1 - num2)
    return sum_result, diff_result

# --- Main: sum_and_diff ---
a, b = sum_and_diff(13, 45)
print("\nSum of the two numbers is", a, "and the difference is", b)
# --- End of Main: sum_and_diff ---


# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# --- Main: factorial ---
x = 10
y = factorial(x)
print(f"\n{x}! = {y}")
# --- End of Main: factorial ---


# Using the calendar module to print a specific month
import calendar

# --- Main: calendar (month) ---
print("\n", calendar.month(2024, 11))
# --- End of Main: calendar (month) ---


# List operations and printing even/odd numbers
L = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# --- Main: List operations ---
print("\nList elements:", end=" ")
for i in range(len(L)):
    print(L[i], end="; ")

print("\n", 40 * "-")

print("Even numbers:", end=" ")
for i in range(len(L)):
    if L[i] % 2 == 0:
        print(L[i], end="; ")

print("\n", 40 * "-")

print("Odd numbers:", end=" ")
for i in range(len(L)):
    if L[i] % 2 != 0:
        print(L[i], end="; ")
print()
# --- End of Main: List operations ---

# Display the whole calendar for a year
print("\n", calendar.calendar(2025))

# Display a specific month from the calendar module
print("\n", calendar.month(2025, 11))

print("我的學號:11344123;姓名:馮郁宸")
print(40*"#")
b=int(input("輸入一個介於2~4的整數:"))
c=int(input("輸入另一個介於7~9的整數:"))
sum=0
for i in range(b,c+1):
    for j in range(b,c+1):
        print("{0}*{1}={2}".format(i,j,(i*j)),end="\t")
        sum=sum+(i*j)

    print()
print("乘法表加總是:",sum)