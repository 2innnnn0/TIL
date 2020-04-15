import os
import gc
import pandas as pd
from google.colab import auth
from google.cloud import bigquery
from google.cloud import storage


class BQ:
    def __init__(self, project_id, wait=True, temp_folder='bq_temp'):
        self.wait = wait
        self.project_id = project_id
        self.temp_folder = temp_folder
        
        auth.authenticate_user()
        self.client = bigquery.Client(project_id)
        self.storage_client = storage.Client(project_id)

    def get(self, query):
        return pd.read_gbq(query, project_id=self.project_id, dialect='standard')

    def wait_job(self, job):
        job.result() if self.wait == True else False
        return job

    def table_ref(self, path):
        dataset_name, table_name = path.split('.')
        return self.client.dataset(dataset_name).table(table_name)

    def run(self, **args):
        job_config = bigquery.QueryJobConfig()
        job_config.destination = args['destination']
        job_config.create_disposition = 'CREATE_IF_NEEDED'
        job_config.write_disposition = 'WRITE_TRUNCATE' # WRITE_TRUNCATE or WRITE_APPEND
        job_config.use_legacy_sql = False
        job_config.allow_large_results = True
        job = self.client.query(args['query'], job_config=job_config)
        return self.wait_job(job)

    def create_table(self, query, table_path):
        table_ref = self.table_ref(table_path)
        create_job = self.run(query = query, destination=table_ref)
        return self.wait_job(create_job)

    def export_csv(self, table_path, destination_uri):
        table_ref = self.table_ref(table_path)
        extract_job = self.client.extract_table(table_ref, destination_uri, location='US')
        return self.wait_job(extract_job)

    def delete_table(self, table_path):
        table_ref = self.table_ref(table_path)
        self.client.delete_table(table_ref)

    def get_blob_list(self, gcs_uri):
        bucket_name, file_path = gcs_uri.replace('gs://', '').split('/', 1)
        bucket = self.storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=file_path)
        return blobs
        
    def download_csv(self, gcs_uri):
        if not os.path.isdir(self.temp_folder): 
            os.mkdir(self.temp_folder)
        blobs = self.get_blob_list(gcs_uri)
        blob_paths = []
        for blob in blobs:
            blob_name = blob.name.split('/')[-1]
            blob_path = f'{self.temp_folder}/{blob_name}'
            blob.download_to_filename(blob_path)
            blob_paths.append(blob_path)
        return blob_paths
                
    def concat_df(self, file_paths):
        dfs = [pd.read_csv(file_name) for file_name in file_paths]
        df = pd.concat(dfs, axis=0, ignore_index=True)
        del dfs
        gc.collect()
        return df

    def download_df(self, gcs_uri):
        files = self.download_csv(gcs_uri)
        df = self.concat_df(files)
        return df