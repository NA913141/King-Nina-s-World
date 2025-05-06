# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: 
This script includes two exam-style problems:
1. Geometry Shape Calculation: Calculates area and perimeter for circles and rectangles.
2. Number Square Generator: Prints 10x10 squares of consecutive odd or even numbers.
User input is handled with simple text prompts for shape and number type selection.
"""

import math  # Import math module to use pi

# -------------------- Exam Question 1: Geometric Shape Calculation --------------------
def print_header(student_id, student_name):
    """
    Prints student ID, name, and a separator line.
    """
    print(f"Student ID: {student_id}, Student Name: {student_name}")
    print("#" * 40)

def calculate_circle(radius):
    """
    Calculates the area and perimeter of a circle.
    """
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius
    return area, perimeter

def calculate_rectangle(length, width):
    """
    Calculates the area and perimeter of a rectangle.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def get_shape_input():
    """
    Gets user input for the shape type (circle or rectangle) and dimensions.
    """
    shape = input("Enter c/C for circle or s/S for rectangle: ")
    shape = shape.lower()

    if shape == 'c':
        radius = float(input("Enter circle radius: "))
        return shape, radius, None, None
    elif shape == 's':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        return shape, length, width, None
    else:
        print("Wrong input")
        return None, None, None, None

def run_geometry_calculation():
    """
    Main function to run the geometric shape calculations.
    """
    student_id = "1123456"  # Replace with your actual student ID
    student_name = "XXX"  # Replace with your actual student name
    print_header(student_id, student_name)

    for _ in range(3):
        shape, dim1, dim2, _ = get_shape_input()

        if shape == 'c':
            area, perimeter = calculate_circle(dim1)
            print(f"Radius = {dim1}, Area = {area:.1f}, Perimeter = {perimeter:.2f}")
        elif shape == 's':
            area, perimeter = calculate_rectangle(dim1, dim2)
            print(f"Length = {dim1}, Width = {dim2}, Area = {area:.1f}, Perimeter = {perimeter:.0f}")
        elif shape is None:
            continue

# -------------------- Exam Question 2: Number Squares --------------------
def print_header_number_square(student_id, student_name):
    """
    Prints student ID, name, and a separator line (for number square problem).
    """
    print(f"Student ID: {student_id}, Student Name: {student_name}")
    print("#" * 40)

def print_odd_square():
    """
    Prints a square of odd numbers.
    """
    num = 1
    for i in range(10):
        for j in range(10):
            print(f"{num:3}", end=" ")
            num += 2
        print()

def print_even_square():
    """
    Prints a square of even numbers.
    """
    num = 2
    for i in range(10):
        for j in range(10):
            print(f"{num:3}", end=" ")
            num += 2
        print()

def get_number_type_input():
    """
    Gets user input for the number type (odd or even).
    """
    choice = int(input("Enter 1 for odd square or 2 for even square: "))
    return choice

def run_number_square_generation():
    """
    Main function to run the number square generation.
    """
    student_id = "1123456"  # Replace with your actual student ID
    student_name = "XXX"  # Replace with your actual student name
    print_header_number_square(student_id, student_name)

    for _ in range(2):
        choice = get_number_type_input()
        if choice == 1:
            print_odd_square()
        elif choice == 2:
            print_even_square()
        else:
            print("Wrong input")

# -------------------- Main Program --------------------
if __name__ == "__main__":
    run_geometry_calculation()
    print("\n" + "-" * 40 + "\n")
    run_number_square_generation()
