import pandas as pd
import numpy as np
import openpyxl

df1 = pd.read_csv("nba.csv")
print(df1)
print(df1.dropna())
df1.to_csv("1.csv")
df1.to_excel("1.xlsx")
