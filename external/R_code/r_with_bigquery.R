library(dplyr)
library(bigrquery)
library(bigQueryR)
library(tidyverse)
billing <- "project_id"
sql.load<-function(sql_string){
  billing <- "project_id"
  bq_auth(path = ".json")
  sql <- sql_string
  tb <- bq_project_query(billing, sql)
  data.set<-bq_table_download(tb, bigint = "character")
  return(data.set)
}
​
sql <- " SELECT * FROM [TALBE] "

# 빅쿼리에서 데이터불러오기
df<-sql.load(sql)
cols = c(10:37,40);    
df[,cols] = apply(df[,cols], 2, function(x) as.numeric(as.character(x)));
​
colnames(cb)[41] <- ""
colnames(cb)[42] <- ""
low_perform<- cb %>% filter ( < )
bqr_auth("~/.json")
bqr_global_project('project_id')
bqr_global_dataset('dataset_name')

# 빅쿼리 테이블로 내보내는 코드
bqr_upload_data(projectId = bqr_get_global_project(),
                datasetId = bqr_get_global_dataset(), 'dataset_name', dataset_name,
                create = "CREATE_IF_NEEDED",
                writeDisposition ="WRITE_TRUNCATE",
                schema = NULL, sourceFormat ="CSV", wait = TRUE, autodetect = FALSE,
                nullMarker = NULL, maxBadRecords = NULL, allowJaggedRows = FALSE,
                allowQuotedNewlines = FALSE, fieldDelimiter = NULL)

