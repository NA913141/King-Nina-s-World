# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: 
This script allows users to calculate the area and perimeter of either a circle or rectangle.
The program prompts user input and performs the calculation accordingly.
"""

print("學號:11344123;姓名:馮郁宸")
print("#" * 40)

shape = input("Enter 'c' for Circle or 's' for Rectangle: ")

if shape.lower() == "c":
    import math
    radius = int(input("Enter radius: "))
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    print(f"Radius = {radius}, Area = {area:.2f}, Perimeter = {perimeter:.2f}")
elif shape.lower() == "s":
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Length = {length}, Width = {width}, Area = {area}, Perimeter = {perimeter}")
else:
    print("Invalid input. Please enter 'c' or 's'.")
