# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: 
This script stores students' scores in three subjects,
calculates total scores per student, and computes average scores per subject.
"""

names = ["John", "Mary", "Tom", "Amy", "Michael"]
subjects = ["Chinese", "English", "Math", "Total"]
grades = [
    [95, 100, 100],
    [86, 90, 75],
    [98, 98, 96],
    [78, 90, 80],
    [70, 68, 72]
]

# Print header
for subject in subjects:
    print(f"\t{subject}", end=" ")
print("\n", "=" * 40)

# Print each student's grades and total
for i in range(len(grades)):
    print(names[i], end="\t")
    total = sum(grades[i])
    for score in grades[i]:
        print(score, end="\t")
    print(total)

print("-" * 45)

# Calculate and print subject averages
for i in range(3):  # Chinese, English, Math
    total = sum(grades[j][i] for j in range(5))
    average = total / 5
    print(f"\t{average:.1f}", end="")
