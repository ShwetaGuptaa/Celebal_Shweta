import pandas as pd
## reading the input file
df=pd.read_csv("input.csv",header=0)
#print(df)
out=[]
#print(df.columns)
#print(df.loc[:,"Country"])
for row in df.index:
    if 'USA' in df.loc[row,"Country"]:
        #print(df.loc[row,:])
        out.append(df.loc[row,:])

#print(out)

## storing data frame into a csv file
out.to_csv('output.csv')
