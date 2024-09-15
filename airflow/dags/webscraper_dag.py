from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dag = DAG(
    'scrape_information',
    description='A DAG to run webscraping script weekly',
    start_date=datetime(2024, 9, 15),
    schedule="@weekly",
    catchup=False
)

# Function to run the webscrape.py script

def print_welcome():
    print('Scraping completed !')

def run_webscrape_script():
    
    try:
        result = subprocess.run(["python", "/opt/airflow/webscrape2.py"], capture_output=True, text=True, check=True)
        logger.info(f"Webscrape output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running webscrape.py: {e}")
        logger.error(f"Script output: {e.output}")
        raise

def run_csv_to_azure():

    try:
        result = subprocess.run(["python", "/opt/airflow/csv_to_azure.py"], capture_output=True, text=True, check=True)
        logger.info(f"CSV to Azure output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running csv_to_azure.py: {e}")
        logger.error(f"Script output: {e.output}")
        raise



# Create a task to run the webscrape script
scrape_task = PythonOperator(
    task_id='run_webscrape_script',
    python_callable=run_webscrape_script,
    dag=dag
)

print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag

)

write_to_azure_task = PythonOperator(
    task_id='csv_to_azure',
    python_callable=run_csv_to_azure,
    dag=dag
)




scrape_task >> print_welcome_task >> write_to_azure_task