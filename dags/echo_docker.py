import os
from datetime import datetime

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sdk import DAG
from airflow.timetables.interval import CronDataIntervalTimetable


with DAG(
    dag_id="echo_docker",
    description="Test DockerOperator",
    start_date=datetime(2026, 1, 1),
    end_date=datetime(2030, 1, 3),
    max_active_tasks=1,  # Limits this DAG to 1 parallel tasks
    max_active_runs=1,    # Limits to 1 active run at a time
    #schedule=CronDataIntervalTimetable("@monthly", "UTC"),
    catchup=True,
):

    echo_docker = DockerOperator(
        task_id="docker_echo_docker",
        #image="models-test:latest",
        image="models-dev:latest",
        command=[
            "uv", 
            "run", 
            "crea_tablas.py"
        ],
        # Explicitly forward the variable here:
        environment={
            ENV : os.environ.get(ENV) for ENV in ENVS_VARS
        },
        #environment={
        #    "RUSTFS_DNS" : os.environ.get("RUSTFS_DNS"), 
        #    "RUSTFS_PORT" : os.environ.get("RUSTFS_PORT"),
        #},
        #env_file = "../.env-dev", 
        # Required settings if Airflow itself runs inside Docker (Docker-in-Docker)
        #docker_url="unix://var/run/docker.sock",
        #auto_remove=True,
        #network_mode="host",
        network_mode="pipeline_data_slv_default"
        # Note: this host path is on the HOST, not in the Airflow docker container.
        #mounts=[Mount(source="docker_airflow-data-volume", target="/data", type="volume")],
        #mount_tmp_dir=False,
    )

    crea_tablas