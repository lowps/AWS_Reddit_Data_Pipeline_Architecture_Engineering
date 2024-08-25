from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys
import pytz

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import reddit_pipeline
from dags.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Erick Lopez',
    'start_date': datetime( 2024, 8, 10)
}
# Define the timezone
timezone = pytz.timezone('America/New_York')
file_postfix = datetime.now(timezone).strftime("%Y%m%d")


#Declaring a DAG, creates a DAG in airflow 
dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags= ['reddit', 'etl', 'pipeline']
)

#extraction from reddit
#Operator, sets up the task to run the callable 
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)
#PythonOperator(): calls a specified python callable/function. OPERATORS create tasks by calling callables, these callables are the 'tasks'
#:DAG: A collection of a multiple tasks are called a DAG
#:Executor: runs all the tasks in a specified order. ex:Celery Executor for distributed tasks

#upload to s3
upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag=dag)

#edges
extract >> upload_s3 

 