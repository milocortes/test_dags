import os
from datetime import datetime

from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.sdk import DAG
from airflow.timetables.interval import CronDataIntervalTimetable
from kubernetes.client import models as k8s

with DAG(
    dag_id="02_kubernetes",
    description="Test Echo on bash using kubernetes",
    start_date=datetime(2026, 1, 1),
    end_date=datetime(2030, 1, 3),
    #schedule=CronDataIntervalTimetable("@daily", "UTC"),
    catchup=True,
    #default_args={"depends_on_past": True},
    max_active_tasks=1,  # Limits this DAG to 1 parallel tasks
    max_active_runs=1,    # Limits to 1 active run at a time
    ) as dag:

    echo_docker = KubernetesPodOperator(
        task_id="echo_docker",
        image="echo-docker:1.0.0",
        #cmds=["fetch-ratings"],
        cmds=[
            "bash", 
            "test.sh"
        ],
        namespace="airflow",
        name="echo-docker",
        #config_file="/opt/airflow/kubeconfig.yaml",
        in_cluster=True,
        image_pull_policy="IfNotPresent",
        is_delete_operator_pod=True,
    )

    echo_docker