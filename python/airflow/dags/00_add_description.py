from datetime import datetime, timedelta
from airflow import models
from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.operators.python_operator import PythonOperator
from dependencies import  add_description

default_args = {
    'owner': 'nathan',
    'depends_on_past': False,
    'start_date': datetime(2020, 2, 1),
    'email': ['your_email@'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'project_id': 'your_project_id'
}

# date_suffix = "{{ macros.ds_format(macros.ds_add(ds, -0), '%Y-%m-%d', '%Y-%m-%d') }}"
date_arrange = "{{ execution_date.replace(second=0, microsecond=0, minute=0, hour=0)}}"

query = f"""
SELECT
    *
FROM table
WHERE
  created_at >= DATE('{date_arrange}')
"""

schema_description = [
    {'name': 'id', 'description': 'id'}
]


date_suffix = "{{ macros.ds_format(macros.ds_add(ds, -0), '%Y-%m-%d', '%Y%m%d') }}"

with models.DAG(
        dag_id='',
        description='',
        schedule_interval='30 0,10 * * *',
        default_args=default_args) as dag:

    bq_task = BigQueryOperator(
        dag=dag,
        bigquery_conn_id='',
        task_id="",
        bql=query,
        use_legacy_sql=False,
        destination_dataset_table=f'project.datasets.table${date_suffix}',
        write_disposition='WRITE_TRUNCATE',
        time_partitioning={'type': 'DAY', 'field': 'date_kr'} # 대문자 해야함
    )

    add_description_task = PythonOperator(
        task_id='description_task',
        python_callable=add_description.update_schema_description,
        op_kwargs={'table_fullname': 'project.datasets.table${date_suffix}',
                   'schema_description': schema_description},
        dag=dag
    )

    bq_task >> add_description_task