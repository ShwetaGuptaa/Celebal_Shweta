import sqlite3

 
import pandas as pd



conn=sqlite3.connect("csvTodb.db")

c=conn.cursor()

print("connection is established")

 



conn.commit()

c.close()

df=pd.read_csv('test.csv',header=0)
print(df)
df.to_sql("csvTodb", conn, if_exists='append', index=False)