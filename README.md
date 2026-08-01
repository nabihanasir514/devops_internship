# 🚀 DevOps Internship Project

## Dockerized Microservices + Kubernetes (Terraform)

---

## 📌 Project Overview

This repository showcases my **DevOps Internship (Week 1 & Week 2)** work, covering:

### 🔹 Week 1 — Microservices with Docker

* Built two Flask-based microservices
* Containerized using Docker
* Enabled service-to-service communication

### 🔹 Week 2 — Kubernetes with Terraform

* Provisioned a local Kubernetes cluster using Terraform
* Managed infrastructure as code (IaC)
* Automated cluster lifecycle (create, destroy, recreate)

---

## 📁 Project Structure

```text
devops-internship/
├── week1/
│   ├── backend-service/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── frontend-service/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── README.md
│
├── week2/
│   ├── main.tf
│   ├── recreate-cluster.sh
│   ├── .terraform.lock.hcl
│   └── (auto-generated)
│       ├── .terraform/
│       └── terraform.tfstate
│
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3.12
* Flask
* Requests
* Docker
* Kubernetes (Minikube)
* Terraform
* kubectl

---

# 🔹 Week 1 — Dockerized Microservices

## 🧩 Architecture

Two services:

* **Frontend Service** → Port `5001`
* **Backend Service** → Port `5002`

The frontend calls the backend via HTTP.

---

## 🔗 Service Communication

```python
response = requests.get("http://localhost:5002/info")
```

### 🔄 Flow

```text
Client → Frontend → Backend → Frontend → Client
```

---

## 🐳 Docker Setup

### Build Images

```bash
cd week1/backend-service
docker build -t backend-service:1.0 .

cd ../frontend-service
docker build -t frontend-service:1.0 .
```

---

### Run Containers

```bash
docker run -d --name backend -p 5002:5002 backend-service:1.0
docker run -d --name frontend -p 5001:5001 frontend-service:1.0
```

---

## ✅ Verification

```bash
docker ps

curl http://localhost:5002/health
curl http://localhost:5002/info

curl http://localhost:5001/health
curl http://localhost:5001/info
curl http://localhost:5001/backend-info
```

---

## 🔐 Non-Root User Check

```bash
docker exec -it frontend whoami
docker exec -it backend whoami
```

Expected:

```text
appuser
```

---

## 🎯 Week 1 Outcome

✔ Built microservices using Flask
✔ Implemented REST endpoints
✔ Enabled inter-service communication
✔ Containerized applications using Docker
✔ Used multi-stage builds
✔ Ensured security via non-root user

---

# 🔹 Week 2 — Kubernetes with Terraform

## ⚙️ Terraform Configuration

```hcl
terraform {
  required_providers {
    minikube = {
      source  = "scott-the-programmer/minikube"
      version = "0.6.0"
    }
  }
}

provider "minikube" {}

resource "minikube_cluster" "my-cluster" {
  driver       = "docker"
  cluster_name = "devops-week2"
  memory       = "2200mb"
  cpus         = 2
}
```

---

## 🚀 Setup

### Initialize

```bash
cd week2
terraform init
```

---

### Plan

```bash
terraform plan
```

---

### Apply

```bash
terraform apply
```

---

## ✅ Cluster Verification

```bash
kubectl cluster-info
kubectl get nodes
kubectl get pods -A
```

---

## 🔗 kubectl Context

```bash
kubectl config current-context
```

Fix if needed:

```bash
minikube update-context -p devops-week2
```

---

## 🔁 Cluster Reset Script

### Usage

```bash
chmod +x recreate-cluster.sh
./recreate-cluster.sh
```

### What it does:

* Destroys Terraform resources
* Removes orphaned Minikube clusters
* Cleans Docker containers
* Resets kubeconfig
* Recreates cluster automatically

---

## 🐞 Issues & Fixes

### Memory Issue (WSL2)

* Reduced memory to `2200mb`
* Updated `.wslconfig`

---

### Terraform Slow Execution

* Verified using:

```bash
docker ps
docker stats
```

---

### kubectl Connection Error

* Fixed using:

```bash
minikube update-context -p devops-week2
```

---

### Orphaned Cluster

* Removed using:

```bash
minikube delete -p minikube
```

---

## 🎯 Week 2 Outcome

✔ Provisioned Kubernetes cluster via Terraform
✔ Verified cluster health
✔ Managed infrastructure as code
✔ Automated cluster reset
✔ Handled real-world DevOps issues

---

# 💡 Key Learnings

* Docker enables portable microservices
* Kubernetes manages container orchestration
* Terraform enables reproducible infrastructure
* Local environments can drift → cleanup is important
* Automation improves reliability and efficiency

---

# 📌 Final Conclusion

This project demonstrates a complete DevOps workflow:

👉 **Week 1:** Build & containerize applications
👉 **Week 2:** Deploy infrastructure using Terraform

Together, they form a strong foundation for:

* Kubernetes deployments
* CI/CD pipelines
* Scalable cloud infrastructure

---

## 🚀 Future Improvements

* Deploy services on Kubernetes (pods + services)
* Add CI/CD pipeline (GitHub Actions)
* Use Helm for deployment
* Move to cloud (AWS / Azure / GCP)

---
