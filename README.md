# Airflow in Kubernetes

Build the Docker images

```bash 
minikube image build -t echo-docker:1.0.0 ./services/echo_bash
```

Deploy and verify the service:
```bash
kubectl apply -f resources/echo_docker.yaml
kubectl rollout status deploy/echo-docker
kubectl get svc echo-docker

```

```bash

```

```bash

```

```bash

```
