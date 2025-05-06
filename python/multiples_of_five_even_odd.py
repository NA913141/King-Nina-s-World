# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 2024
Last Modified on Sat May  6 2025
@author: Nina Feng
@description: 
This script generates an array of the first 10 multiples of 5,
then prints all values, even numbers, and odd numbers separately.
"""

A = [(i + 1) * 5 for i in range(10)]

print("All values:")
for value in A:
    print(value, end=";")

print("\nEven: ", end="  ")
for value in A:
    if value % 2 == 0:
        print(value, end=";")

print("\nOdd: ", end="  ")
for value in A:
    if value % 2 != 0:
        print(value, end=";")
