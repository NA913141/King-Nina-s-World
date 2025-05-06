# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: 
This script generates a list of 10 random integers between 1 and 100,
prints the list, sorts it in ascending order, and prints the sorted list.
"""

import random

Ar = [random.randint(1, 100) for _ in range(10)]

print("Original List:")
for value in Ar:
    print(value, end=";")

Ar.sort()
print("\nSorted List:")
print(Ar)
