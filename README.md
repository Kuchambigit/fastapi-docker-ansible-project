# FastAPI Docker Ansible Project

## Project Overview

This project demonstrates a real-world DevOps workflow using:

- Python FastAPI
- Docker
- Ansible
- Linux Automation
- GitHub Version Control

The application is containerized with Docker and automatically deployed to multiple Linux servers using Ansible.

---

# Technologies Used

## Backend
- Python 3
- FastAPI
- Uvicorn

## DevOps & Automation
- Docker
- Ansible
- Git
- GitHub

## Operating System
- Ubuntu Linux

---

# Project Architecture

Control Node:
- Runs Ansible playbooks
- Automates deployment to target servers

Managed Nodes:
- Node 1 (Dev)
- Node 2 (Prod)

Docker:
- Builds FastAPI container image
- Runs application containers

Ansible:
- Installs Docker automatically
- Builds Docker images
- Deploys containers
- Uses separate inventories for Dev and Prod

---

# Features

- Automated Docker installation
- Automated container deployment
- FastAPI application deployment
- Environment-specific inventories
- Ansible role-based structure
- Infrastructure automation
- Multi-node deployment

---

# Project Structure

```text
python-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── docker-deploy.yml
├── inventories/
│   ├── dev/
│   └── prod/
├── roles/
│   └── docker/
│       ├── tasks/
│       ├── handlers/
│       ├── templates/
│       └── files/
webhook test
poll scm test

# FastAPI DevOps Platform Project

## Overview
This project demonstrates a complete DevOps workflow using:

- FastAPI
- Docker
- Kubernetes (K3s)
- Helm Charts
- Prometheus Monitoring
- Grafana Dashboards

## Features

- Containerized FastAPI application
- Kubernetes deployments and services
- Helm-based application packaging
- Prometheus metrics endpoint
- Grafana observability dashboards
- Node Exporter monitoring

## Technologies

- Python
- FastAPI
- Docker
- K3s
- Helm
- Prometheus
- Grafana

## Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

## Helm Deployment

```bash
helm install fastapi-release ./fastapi-chart
```

## Monitoring

Metrics endpoint:

```text
/metrics
```

Grafana dashboard available on port 3000.

## Project Structure

```text
ansible-lab/
├── fastapi-chart/
├── k8s/
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```
