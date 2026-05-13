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
