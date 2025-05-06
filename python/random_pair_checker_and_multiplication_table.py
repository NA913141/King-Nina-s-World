# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 2024
Last Modified on Sat May  3 2025

@author: Nina Feng
@description: This script generates random integer pairs and checks their parity (even/odd),
              then prompts the user to input two numbers to generate a multiplication table
              and calculates the total sum of all products.
"""

import random

# Generate and check four pairs of random integers
for i in range(1, 5):
    print(f"No.{i}-------")

    # Generate two random integers between 1 and 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Display the generated numbers
    print("Two random numbers (1-100):", num1, "and", num2)

    # Determine and print the parity of the numbers
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both numbers are even.")
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print("Both numbers are odd.")
    else:
        print("One number is even and the other is odd.")


# Define a function to print the multiplication table and calculate the total sum
def multiplication_table(num1, num2):
    """
    Generate a num1 x num2 multiplication table and return the sum of all products.

    Args:
        num1 (int): number of rows
        num2 (int): number of columns

    Returns:
        int: total sum of all products in the table
    """
    total_sum = 0
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            print(f"{i}*{j}={i*j:3}", end=" ")  # Print product with fixed width
            total_sum += i * j
        print()  # Newline after each row
    return total_sum


# Get user information
student_id = input("Enter your student ID: ")
student_name = input("Enter your name: ")

# Separator line
print("#" * 40)

# Run the multiplication table function twice with user input
for _ in range(2):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print(f"Multiplication Table ({num1} x {num2}):")
    result = multiplication_table(num1, num2)
    print(f"Total sum of products: {result}")
    print("#" * 40)


