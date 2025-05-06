# -*- coding: utf-8 -*-
"""
Created on Wed Jun 1 2025
Last Modified on Sat May  6 2025

@author: Nina Feng
@description:
This script contains several independent sections:
1. Currency conversion from USD to TWD.
2. Reading a resume text file.
3. Calculating and writing BMI information to a text file.
4. Summing numbers from 1 to 100.
5. A number guessing game.
6. Printing a star pyramid based on user input height.
"""

# =============================
# 1. USD to TWD Conversion
# =============================
fe = float(input("請輸入美金對台幣的匯率: "))
us = float(input("請輸入美金: "))
nt = us * fe
print("台幣 = ", round(nt, 1), "元")
# round is used to round the number to 1 decimal place

# =============================
# 2. Read Resume File
# =============================
try:
    infile = open("C:/pythonpractice/resume.txt", "r", encoding="utf-8")
    print("讀取檔案顯示:")
    print(infile.read())
    infile.close()
except FileNotFoundError:
    print("找不到 resume.txt，請確認檔案路徑是否正確。")

# =============================
# 3. Calculate and Write BMI
# =============================
h, w = map(float, input("請輸入身高(公分), 體重(公斤): ").split(","))
bmi = round(w / ((h / 100) ** 2), 2)

outfile = open("C:/pythonpractice/bmi.txt", "w", encoding="utf-8")
outfile.write("**************\n")
outfile.write("姓名: Allen\n")
outfile.write("身高: " + str(h) + "\n")
outfile.write("體重: " + str(w) + "\n")
outfile.write("我的BMI: " + str(bmi) + "\n")
outfile.write("**************\n")
outfile.write("BMI是指身體質量指數，如果BMI小於18，表示過輕；如果是介於18至24之間表示標準；如果是超過24表示過重了\n")
outfile.close()

infile = open("C:/pythonpractice/bmi.txt", "r", encoding="utf-8")
print("讀取檔案顯示:")
print(infile.read())
infile.close()

# =============================
# 4. Sum from 1 to 100
# =============================
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("1 到 100 的總和為:", total)

# =============================
# 5. Number Guessing Game
# =============================
import random
number = random.randint(1, 100)
while True:
    guess = int(input("請輸入一個數字(介於1 ~ 100): "))
    if guess == number:
        print("您猜中了")
        break
    elif guess < number:
        print("請猜大一些")
    else:
        print("請猜小一些")

# =============================
# 6. Star Pyramid
# =============================
n = int(input("請輸入金字塔的高度: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
