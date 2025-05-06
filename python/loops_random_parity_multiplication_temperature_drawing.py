# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 2024
Last Modified on Sat May  3 2025

@author: Nina Feng
@description: This script covers basic loop practice, random number parity checking,
              multiplication tables, temperature conversion, and drawing functions.
"""

import random

# ---------------- Part 1: Print numbers from 1 to 20, skipping multiples of 5 ----------------
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i, end=";")
print("\nStudent ID: 11344123; Name: Nina Feng")
print("#" * 40)

# ---------------- Part 2: Random number pairs and parity checking ----------------
for i in range(1, 5):
    print(f"No.{i}-------")
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("Two random numbers (1-100):", num1, "and", num2)

    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both numbers are even.")
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print("Both numbers are odd.")
    else:
        print("One is even and the other is odd.")

# ---------------- Part 3: Multiplication table generator ----------------
def multiplication_table(num1, num2):
    """Generates a multiplication table and returns the sum of all products."""
    total_sum = 0
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            print(f"{i}*{j}={i*j:3}", end=" ")
            total_sum += i * j
        print()
    return total_sum

print("Student ID: 11344123; Name: Nina Feng")
print("#" * 40)

# Execute multiplication table 2 times with user input
for _ in range(2):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"Multiplication Table ({num1} x {num2}):")
    result = multiplication_table(num1, num2)
    print(f"Total Sum of Products: {result}")
    print("#" * 40)

# ---------------- Part 4: While loop to sum numbers from 0 to 100 ----------------
i = 0
total = 0
while i <= 100:
    total += i
    i += 1
print("Sum from 1 to 100:", total)

# ---------------- Part 5: Skip multiples of 5 again ----------------
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i, end=";")
print()

# ---------------- Part 6: Temperature conversion ----------------
def c2f(a):
    """Convert Celsius to Fahrenheit and print the result."""
    f = a * 1.8 + 32
    print(f"{a}°C converts to {f}°F")

c2f(55)

def c2f_ki(a):
    """Convert Celsius to Fahrenheit and return the result."""
    f = a * 1.8 + 32
    return f

# ---------------- Part 7: Drawing functions ----------------
def draw(b):
    """Draw a line of '=' characters."""
    print(b * "=")

def draw2(a, k):
    """Draw a repeated pattern using multiplication."""
    print(a * k)

def draw3():
    """Draw a fixed line of '@' characters."""
    print(56 * "@")

# Test drawing and conversion
draw(56)
print("Answer   ", c2f_ki(23))
draw(56)


