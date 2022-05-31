import pickle
import numpy as np
import pandas as pd

# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sr1 = pd.Series(list1)
# print(sr1)
# print(sr1[:4])

# sr2 = pd.Series(list1,index=['a','b',"c",'d','e','f','g','h','i','j'])
# print(sr2)
# print(sr2.loc['e'])
# print(sr2.iloc[5])
# print(sr2.add(5))
# print(sr2.mean())
# print(sr2.std())
# print(pd.concat([sr1,sr2]))

# list1 = ["Hello","World"]
# df1 = pd.DataFrame(list1)
# print(df1,"\n")

# dict1 = {"Name":["Distance","Time","Mass"],"Unit":["meter","second","kilogram"]}
# df2 = pd.DataFrame(dict1)
# print(df2,"\n")
# print(df2.index)

# df3 = pd.read_csv("nba.csv",index_col="Team")
# print(df3,"\n")
# print(df3["Name"],"\n") # According to column name
# print(df3.loc[["Boston Celtics","Utah Jazz"]],"\n") # according to row header
# print(df3.loc[["Boston Celtics","Utah Jazz"],["Age", "Height",  "Weight"]],"\n") # according to row header
# print(df3.iloc[[0,1,-1]])
# print(df3.iloc[[0,1,-1],[0,2,6]])
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

# for i in df5.iteritems():
# 	print("\n",i,"\n")

# for i in df5.itertuples():
# 	print("\n",i,"\n")

# for i in df5.iterrows():
# 	print("\n",i,"\n")

# for i in df5:
# 	print(df5[i])


# dict4 = {'First Score':[99, 85, 85, 96],
# 		'Second Score': [45, 86, 56, 49],
# 		'Third Score':[57, 40, 85, None]}
# df6 = pd.DataFrame(dict4)
# df6.insert(3,'Fourth Score',value=[45,56,78,98])
# print(df6)
# # print(df6.query('"First Score" < "Second Score"')) # Doesn't work With space
# print(df6.add(1,fill_value=52))
# print(df6.sub(1))
# print(df6.mul(2))
# print(df6.div(2))
# print(df6.nunique())
# print(df6.astype(float))
# print(df6.sort_values('First Score'))
# print(df6.sort_values(['First Score','Second Score','Third Score']))
# print(df6.rename(columns={'First Score':1,'Second Score':2,'Third Score':3,'Fourth Score':4}))
# print(df6.shape)
# print(df6.ndim)
# print(df6.rank())

# df7 = pd.DataFrame({"L1":[45,89,12,36],"L2":[74,89,36,52],"L3":[12,74,32,89]})
# df8 = pd.DataFrame({"R1":[1,5,9],"R2":[2,6,10],"R3":[3,7,11],"R4":[4,8,12]})
# print(df7)
# print(df8)
# print(df7.dot(df8))
# print(df7.__matmul__(df8)) # Matrix Multiplication
# print(df7.__rmatmul__(df8)) # Transpose of matrix then Matrix Multiplication
# print(df7.to_numpy())
# print(df7.to_dict())
# print(df7.to_clipboard())
# print(df7.to_html())
# print(df7.to_json())
# print(df7.to_pickle("1.pkl"))
# print(pickle.load(open("1.pkl",'rb')))
# print(df7.nlargest(n=2,columns=2))
# print(df7.transform(func=lambda x:x%10))
# print(df7.append(df8))
# print(pd.concat([df7,df8]))
# print(df7.join(df8,lsuffix="L",rsuffix="R"))

# df9 = pd.DataFrame({"A":[10,52,8,63,7],"B":[41,98,36,74,52],"C":[32,96,36,58,92]},index=[True,False,True,False,True])
# print(df9)
# print(df9.loc[True])
# print(df9.iloc[1])
# print(df9[[False,True,False,True,False]])
# print(df9['A']>10)
# print(df9.min())
# print(df9.min(axis=1))
# print(df9.max())
# print(df9.max(axis=1))
# print(df9.mean())
# print(df9.mean(axis=1))
# print(df9.std())
# print(df9.std(axis=1))
# print(df9.describe())
# print(df9.set_index("A"))
# print(df9.reset_index())
# print(df9.idxmin())
# print(df9.idxmin(axis=1))
