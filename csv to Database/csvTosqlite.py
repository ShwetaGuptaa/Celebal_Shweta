import sqlite3
from sqlite3 import Error
import pandas as pd
df=pd.read_csv('test.csv',header=0)
print(df)
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c=conn.cursor()
        #print(sqlite3.version)
        df.to_sql("csvTodb", conn, if_exists='append', index=False)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    

if __name__ == '__main__':
    create_connection("pythonsqlite.db")
#r"C:\sqlite\