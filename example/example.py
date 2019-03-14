#!/usr/bin/env python

import airflow
from airflow.models import DAG
from airflow.operators.glue_presto_apas import GluePrestoApasOperator
from datetime import timedelta

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    dag_id='example-dag',
    schedule_interval='0 0 * * *',
    default_args=args,
)

GluePrestoApasOperator(
        task_id='example-task',
        schema='example-schema',
        table='example-schema',
        sql='',
        catalog_region_name='ap-northeast-1',
        dag=dag,
        )

if __name__ == "__main__":
    dag.cli()
