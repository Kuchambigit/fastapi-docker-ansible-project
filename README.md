# FastAPI DevOps Platform Project

## Overview

This project demonstrates a complete end-to-end DevOps platform built with modern cloud-native tools and automation practices.

The application is a containerized FastAPI service deployed on Kubernetes (K3s) with automated CI/CD pipelines, monitoring, observability, Helm packaging, and infrastructure automation.

---

# Technologies Used

## Backend
- Python 3
- FastAPI
- Uvicorn

## DevOps & Automation
- Docker
- Jenkins
- Ansible
- Helm
- Kubernetes (K3s)
- Git
- GitHub

## Monitoring & Observability
- Prometheus
- Grafana
- Node Exporter

## Operating System
- Ubuntu Linux

---

# CI/CD Pipeline

This project uses Jenkins for CI/CD automation.

Pipeline workflow:

```text
GitHub
   ↓
Jenkins Pipeline
   ↓
Docker Build
   ↓
DockerHub Push
   ↓
Ansible Deployment
   ↓
Kubernetes (K3s)
```

### Jenkins Features

- Automated Docker image builds
- DockerHub integration
- Kubernetes deployments
- Helm chart deployments
- GitHub SCM polling

---

# Kubernetes Features

- Kubernetes Deployments
- Services
- Ingress with Traefik
- Helm Chart packaging
- Rolling deployments
- Local DNS routing

Application endpoint:

```text
http://fastapi.local/docs
```

Metrics endpoint:

```text
http://fastapi.local/metrics
```

---

# Monitoring Stack

The monitoring stack includes:

- Prometheus metrics collection
- Grafana dashboards
- Kubernetes node monitoring
- FastAPI application metrics
- Node Exporter integration

Grafana Dashboard:

```text
http://192.168.1.153:3000
```

---

# Project Structure

```text
ansible-lab/
├── fastapi-chart/
├── k8s/
├── inventories/
├── roles/
├── main.py
├── Dockerfile
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

# Helm Deployment

Install the application using Helm:

```bash
helm install fastapi-release ./fastapi-chart
```

---

# Kubernetes Deployment

Deploy manually using Kubernetes manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

---

# Features

- Containerized FastAPI application
- Kubernetes orchestration
- Helm-based deployments
- Jenkins CI/CD automation
- DockerHub integration
- Prometheus monitoring
- Grafana dashboards
- Ingress routing with Traefik
- Infrastructure automation with Ansible

---

# Future Improvements

- ArgoCD GitOps workflows
- TLS/HTTPS with Traefik
- Horizontal Pod Autoscaling
- Multi-environment Helm values
- AWS EKS deployment
- Centralized logging with Loki
