import pandas as pd
import pymysql
from time import time
from time import sleep

## db connect function
def mysql_connection(query) :
    if var == "" :
        a = "df"
    else :
        a = (var+"_df")

    # db connect
    nz_con = pymysql.connect(user="id", password="password", host="121.XXX.XXX.XX",
                            database="db", port=3306, charset="utf8")

    t1 = time()
    df = pd.read_sql(query, con=nz_con)
    globals()[a] = df
    print(df)
    print("\n")
    print(query, "\nquery %0.3fm : " % ((time()-t1)/60), " / create variable : ",a)

    # db connect exit
    nz_con.close()

# query
query = """
        select 
            *
        from
            table
        """

var = ""
mysql_connection(query)
df.to_csv("remote_mysql.csv", sep=",")
