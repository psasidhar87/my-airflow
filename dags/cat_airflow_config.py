from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
#with DAG(dag_id="airflow_cfg", schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
dag_name='airflow_configurations'
with DAG(dag_name,
         start_date=days_ago(1),
         schedule_interval='20 13 * * *',
         catchup=False
         ) as dag:
    cli_command = BashOperator(
        task_id="bash_command",
        bash_command="cat /usr/local/airflow/airflow.cfg"
    )

    task2 = BashOperator(
	task_id="env_command",
	bash_command="env"
    )

cli_command >> task2