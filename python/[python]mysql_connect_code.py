# full code
import pymysql
import pandas as pd


# 1. Mysql 접속
def mysql_query():
    conn=pymysql.connect(host="",
    port=3306,
    db="",
    user="",
    passwd="")
    curs=conn.cursor()
    sql=   """ SELECT * FROM [] """
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    conn.commit()
    conn.close()

# 2. 데이터 조회.
if **name**=="**main**":
    df = mysql_query()


# 3. 데이터 저장
df.to_csv('../.csv', index_col= False)