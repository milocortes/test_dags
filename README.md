# Airflow in Kubernetes

To run Apache Airflow on Minikube, use the Official Apache Airflow Helm Chart to deploy its core components. Minikube requires extra CPU and memory resources to handle Airflow's webserver, scheduler, and database backends smoothly.

Follow this step-by-step guide to get Airflow opperational on your local cluster.



## 1. Initialize Minikube with Extra Resources

Airflow is resource-heavy. Allocate at least 4 CPUs and 8GB of RAM.

```bash
minikube start --cpus 4 --memory 8192
```

## 2. Add and Update the Airflow Helm Repository

Use Helm to fetch the official repository maintained by the Apache Airflow community.

```bash
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow \
--timeout 20m0s \
--create-namespace \
--namespace airflow \
--debug --set apiServer.service.type=LoadBalancer -f /etc/helm/values/04-dags-in-git-values.yaml --set postgresql.image.repository=postgres --set postgresql.image.tag=16 
```

## 3. Verify the Running Pods

Monitor the deployment until the webserver, scheduler, and PostgresSQL pods transition into a Running status

```bash
kubectl get pods -n airflow
```

## 4. Access the Airflow Web UI

Minikube isolates container networks from your local machine. Use port forwarding to bridge the connection to your local browser

```bash
kubectl port-forward svc/airflow-api-server 8080:8080 --namespace airflow
```

Open http://localhost:8080 in your browser. Use the default credentials admin for both the username and password to log in.

## 5. How to Sync your DAGs

To add your custom workflows, you can pick one two paths:

- Git-Sync : Pass a Git repository URL directly into your Helm chart parameters. The scheduler will automatically pull code changes from your remote repository.

## 6. Build the Docker images


```bash 
minikube image build -t echo-docker:1.0.0 ./services/echo_bash
```

Deploy and verify the service:
```bash
kubectl --namespace airflow  apply -f resources/echo_docker.yaml
kubectl rollout status deploy/echo-docker
kubectl get svc echo-docker

```


### Delete deployments

Delete a specific deployment:
```bash
kubectl delete deployment <deployment-name>
```

Delete from a specific namespace:
```bash
kubectl delete deployment <deployment-name> -n <namespace-name>
```

Delete using a YAML configuration file:
```bash
kubectl delete -f <filename>.yaml
```

Delete all deployments in the current namespace:
```bash
kubectl delete deployments --all
```


### Delete a container image from your local minikube cluster
```bash
minikube image rm <image-name>
```