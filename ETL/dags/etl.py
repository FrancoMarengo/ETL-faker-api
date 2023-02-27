"""
DAG de Apache Airflow que corre el proceso de extracción, transformación y carga.

"""
from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Se crea el DAG para el proceso ETL.
dag = DAG(
    dag_id = "extract_transform_load",
    start_date = datetime(2023, 2, 25),
    default_args = {
      "depends_on_past": False,
      "email": ["francomarengo.21@gmail.com"],
      "email_on_failure": False,
      "retries": 1,
      "retry_delay": timedelta(minutes=1)
    },
    #                   Minutos  Horas  Dias  Meses  Dias_de_la_semana  
    schedule_interval = '*/30    10-18  *     *      *'                 
)

# Ruta para llegar al archivo de configuración de extracción.
config = os.path.join("scripts", "extract", "data.conf")

# Se define la tarea de extraer, como un BashOperator que utiliza el tap anteriormente creado y target-csv de Singer.
extract = BashOperator(
  task_id="extract", 
  bash_command="tap-faker-api | target-csv --config %s" %config,
  dag=dag
)