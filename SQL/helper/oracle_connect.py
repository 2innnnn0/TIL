import pandas as pd
import cx_Oracle
from time import time
from time import sleep

## db connect function
def oracle_connection(query) :
    if var == "" :
        a = "df"
    else :
        a = (var+"_df")
    # db connect
    dsn = cx_Oracle.makedsn("121.XX.XXX.XX", 1521, sid = "company")
    con = cx_Oracle.connect('id', 'password', dsn, encoding = "UTF-8", nencoding = "UTF-16")
    con.autocommit = True
    t1 = time()

    df = pd.read_sql(query, con=con)
    globals()[a] = df
    print(df)
    print("\n")
    print(query, "\nquery %0.3fm : " % ((time()-t1)/60), " / create variable : ",a)

    # db connect exit
    con.close()

# query
query = """
        select 
            *
        from
            table
"""
var = ""
oracle_connection(query)
df.to_csv("remote_oracle.csv", sep=",")