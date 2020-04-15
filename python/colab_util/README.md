(출처:https://github.com/tommybebe/colab_util/blob/master/README.md)
## Google Colaboratory Utility

- 개인적으로 자주 쓰는 함수들을 모아두었습니다. 
- [Example notebook link](https://colab.research.google.com/drive/1kNj9YNe6dKJgcaAvJ4pwqTcBe5B9fLuM)를 참고해주세요.  

### Bigquery

- 빅쿼리에서 쿼리 결과를 dataframe으로 받아오거나 
- 테이블 생성과 내보내기, 삭제 등을 묶어두었습니다.  
 
#### Initialize
```python
from bigquery import BQ
 
bq = BQ('my-project')
```
#### Get dataframe with query string
```python
bq.get("""
    SELECT * FROM `bigquery-public-data.samples.shakespeare`  
""")
bq.head()
```

#### Create table with query string
```python
job = bq.create_table(
    'SELECT * FROM `bigquery-public-data.samples.shakespeare`',
    'dataset.table'
)
job.state # => 'DONE'
```

#### Export bigquery table to google storage
```python
job = bq.export_csv(
    'dataset.table', 
    'gs://my-bucket/dataset/table.csv'
)
job.state # => 'DONE'
```

#### Download csv as a dataframe
```python
df = bq.download_df('gs://my-bucket/dataset/table.csv')
df
```

#### Delete table
```python
job = bq.delete_table('temp.test1')
job.state # => 'DONE'
```

### Facets

- 데이터 훑어보기 도구입니다. 손쉽게 데이터의 생김새를 파악할 수 있게 해줍니다.
- overview는 데이터의 분포를, dive는 데이터를 여러 축으로 나눠 엘리먼트 단위로 뜯어볼 수 있습니다.      

#### Initialize
```python
import facets
import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
```

#### Overview
```python
facets.overview({
    'train': df.sample(1000),
    'test': df.sample(1000)
})
```

#### Dive
```python
facets.dive(df.sample(1000))
```