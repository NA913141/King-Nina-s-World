# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: 
This script demonstrates various file I/O operations:
1. Writing to and appending text in files using absolute paths.
2. Reading content from text files using different methods.
3. Using 'with' context manager to ensure files are properly closed.
"""

# Write to a file (overwrites if it exists)
f1 = open("c:/aa/bb/cc/test.txt", "w")
f1.write("IIIIIIIII,ld,ep\n")
f1.close()

# Append to the same file
f1 = open("c:/aa/bb/cc/test.txt", "a")
f1.write("IIIIIIIII,ld,ep 2 \n")
f1.close()

# Append using 'with' context manager (creates file if not exists)
with open("c:/aa/bb/cc/test3.txt", "a+") as f1:
    f1.write("IIIIIIIII,ld,ep 2222 \n")

# Write multiple lines to a file using 'writelines'
text = [
    "CYCU is a great university.\n",
    "Teacher Max is excellent.\n",
    "I am also excellent.\n"
]

with open("c:/aa/bb/cc/test4.txt", "w") as f1:
    f1.writelines(text)

# Read and print entire content of test4.txt
with open("c:/aa/bb/cc/test4.txt", "r") as f1:
    print(f1.read())

# Read test4.txt line-by-line using readline and a while loop
with open("c:/aa/bb/cc/test4.txt", "r") as f1:
    line = f1.readline()
    while line != "":
        print(line, end="")  # 'end' prevents double newlines
        line = f1.readline()

