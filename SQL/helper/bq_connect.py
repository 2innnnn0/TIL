import pandas as pd
from time import time
from time import sleep

## db connect function

def bq_connection(query) :
    if var == "" :
        a = "df"
    else :
        a = (var+"_df")
    # db connect
    project = 'project_name'
    projectId = 'project_id'
    dataset_name = ""
    credential_key = '/credential/key.json'

    t1 = time()
    df = pd.read_gbq(query=query, project_id=projectId, private_key=credential_key, dialect='standard')
    globals()[a] = df
    print(df)
    print("\n")
    print(query, "\nquery %0.3fm : " % ((time()-t1)/60), " / create variable : ",a)

# query
query = """
    #standardSQL
    SELECT * FROM `table`
"""
var = ""

bq_connection(query)
df.to_csv("remote_bigquery.csv", sep=",")