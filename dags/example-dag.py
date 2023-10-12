from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.decorators import task

# Define a function that will be executed by PythonOperator
def extract_data():
    # Your data extraction logic here
    print("extract data")

def transform_data():
    # Your data transformation logic here
    print("transform data")

def load_data():
    # Your data loading logic here
    print("load data")

with DAG(
    dag_id="example-dag",
    start_date=datetime(2022, 1 , 1),
    schedule_interval=None,  
    tags=['etl', 'example']
 ) as dag:
    
    # Create task instances for each step
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

# Define the order of task execution
extract_task >> transform_task >> load_task
