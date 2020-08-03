import pandas as pd
import numpy as np
from numpy import nan
data = [[0.04,  nan,  nan, 0.25,  nan, 0.43, 0.71, 0.51,  nan,  nan],
        [ nan,  nan,  nan, 0.04, 0.76,  nan,  nan, 0.67, 0.76, 0.16],
        [ nan,  nan, 0.5 ,  nan, 0.31, 0.4 ,  nan,  nan, 0.24, 0.01],
        [0.49,  nan,  nan, 0.62, 0.73, 0.26, 0.85,  nan,  nan,  nan],
        [ nan,  nan, 0.41,  nan, 0.05,  nan, 0.61,  nan, 0.48, 0.68]]
columns = list('abcdefghij')
df = pd.DataFrame(data, columns=columns)
# df1=df.transpose()
#print(df1)
a="NAN"
df1=df.fillna(a)
print(df1)
check=df.isnull().values
# # print(check)
# df_check=pd.notnull(data)
df_check = pd.DataFrame(check, columns=columns)
# # print(df_check)
# df_train_to_use = df[df.isnull() == True]
# print(df_train_to_use)
for row in df_check.index:
    count=0
    for col in df_check.columns:
        if  df_check.loc[row,col]==True:
            count+=1
            if count==3:
                print("In "+str(row)+"th row third nan is present in column : "+str(col))
#print(df['a'].isnull().values)
# count_nan = df.loc[df['a']=='Yes'].count()
# for col in df.columns:
    # asd=df[col].isnull().values
    # print(asd)
    # print(col)
        # print(count)
        # count+=1
        # # if df.loc[row,:].isnull().values:
            # count=count+1
# print(count)