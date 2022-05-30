import numpy as np
import pandas as pd

# list1 = ["Hello","World"]
# df1 = pd.DataFrame(list1)
# print(df1,"\n")

# dict1 = {"Name":["Distance","Time","Mass"],"Unit":["meter","second","kilogram"]}
# df2 = pd.DataFrame(dict1)
# print(df2,"\n")

# df3 = pd.read_csv("nba.csv",index_col="Team")
# print(df3,"\n")
# print(df3["Name"],"\n") # According to column name

# print(df3.loc[["Boston Celtics","Utah Jazz"]],"\n") # according to row header
# print(df3.loc[["Boston Celtics","Utah Jazz"],["Age", "Height",  "Weight"]],"\n") # according to row header

# print(df3.iloc[[0,1,-1]])
# print(df3.iloc[[0,1,-1],[0,2,6]])

# print(df3.ix["Boston Celtics"])
# print(df3.head(10))
# print(df3.tail(10))


# dict2 = {'First Score':[99, np.nan, np.nan, 96],
# 		'Second Score': [30, 45, 56, 48],
# 		'Third Score':[np.nan, 40, 85, 45]}
# df4 = pd.DataFrame(dict2)
# print(df4,"\n")
# print(df4.isnull(),"\n")
# print(df4.dropna(axis=1),"\n")
# print(df4.fillna(70),"\n")
# print(df4.interpolate(method="linear",limit_direction="both"))
# print(df4.replace(to_replace=30,value=50))

# dict3 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
# 		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
# 		'score':[90, 40, 80, 98]}
# df5 = pd.DataFrame(dict3)
# print(df5)

# for i in df5.iterrows():
# 	print("\n",i,"\n")

# for i in df5:
# 	print(df5[i])

dict4 = {'First Score':[99, 85, 74, 96],
		'Second Score': [30, 86, 56, 49],
		'Third Score':[57, 40, 85, None]}
df6 = pd.DataFrame(dict4)
df6.insert(3,'Fourth Score',value=[45,56,78,98])
print(df6)
print(df6.add(1,fill_value=52))

