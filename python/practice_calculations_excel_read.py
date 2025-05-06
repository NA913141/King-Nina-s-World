# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 2024
Last Modified on Sat May  6 2025

@author: Nina Feng
@description: 
This script contains four small practice tasks:
1. Calculate the volume of a sphere given its radius.
2. Convert USD to TWD using a given exchange rate.
3. Calculate the Euclidean distance between two points.
4. Read and display Excel sheets using pandas.
"""

# Student ID
# 11344123

# ======================
# Practice 1: Sphere Volume
# ======================
from math import pi, pow

r = float(input("請輸入半徑: "))  # Input radius
volume = (4 / 3) * pi * pow(r, 3)   # Volume formula
print("球的體積 =", round(volume, 2))

# ============================
# Practice 2: USD to TWD Conversion
# ============================
exchange_rate = float(input("請輸入美金對台幣的匯率: "))  # Exchange rate
usd = float(input("請輸入美金: "))                         # Amount in USD
ntd = usd * exchange_rate
print("台幣 =", round(ntd, 1), "元")

# ============================
# Practice 3: Distance Between Two Points
# ============================
from math import sqrt

print("請輸入第一個點的 x 和 y（以空格分隔）:")
x1, y1 = map(float, input().split())
print("請輸入第二個點的 x 和 y（以空格分隔）:")
x2, y2 = map(float, input().split())

distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("兩點距離 =", round(distance, 4))

# ============================
# Practice 4: Read Excel Sheets using pandas
# ============================
import pandas as pd

try:
    df1 = pd.read_excel("C:\\Users\\User\\Desktop\\Excel_Score.xlsx", sheet_name="成績計算表")
    df2 = pd.read_excel("C:\\Users\\User\\Desktop\\Excel_Score.xlsx", sheet_name="成績查詢")

    print("\n成績計算表:")
    print(df1.to_string(index=False))

    print("\n成績查詢:")
    print(df2.to_string(index=False))

except FileNotFoundError:
    print("找不到 Excel 檔案，請確認路徑是否正確。")
except Exception as e:
    print("讀取 Excel 時發生錯誤：", e)