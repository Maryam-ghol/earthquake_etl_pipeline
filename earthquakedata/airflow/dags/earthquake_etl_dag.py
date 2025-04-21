from airflow import DAG
from airflow.operators.python import PythonOperator
import os
import pandas as pd
from datetime import datetime
import src.data.make_dataset as fetch_data
import src.features.build_features as process_data
import src.data.load_data as load_data
from pathlib import Path

def fetch_earthquake_data():
    data = fetch_data.fetch_earthquake_data()
    fetch_data.save_data(data)

def process_earthquake_data():
    df = process_data.process_earthquake_data()
    process_data.save_processed_data(df)

def load_earthquake_data():
    base_path = Path(__file__).resolve().parents[2]
    processed_path = base_path / "data" / "processed" / "processed_earthquake_data.csv"
    df = pd.read_csv(processed_path)
    load_data.load_data_to_db(df)

with DAG(
    'earthquake_etl_dag',
    default_args={'owner': 'airflow'},
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    fetch_data_task = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_earthquake_data
    )
    
    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_earthquake_data
    )

    load_data_task = PythonOperator(
        task_id='load_data',
        python_callable=load_earthquake_data
    )

    fetch_data_task >> process_data_task >> load_data_task
