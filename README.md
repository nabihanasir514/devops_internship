Absolutely. I’ll keep your existing **Weeks 1–3 structure and wording**, and add **Week 4 — Helm** based on the Week 4 work in the uploaded material. The Week 4 section will cover the Helm chart structure, installation, upgrade, rollback, and troubleshooting. 

# DevOps Internship Project

## Dockerized Microservices → Kubernetes → Terraform → Helm

---

## 📌 Project Overview

This repository showcases a complete **4-week DevOps learning journey**, where a microservices application is:

* Built using Python (Flask)
* Containerized using Docker
* Deployed on Kubernetes
* Provisioned using Terraform (Infrastructure as Code)
* Packaged and managed using Helm

---

## 🧠 Project Flow

```text
Week 1 → Build & Dockerize Microservices
Week 2 → Provision Kubernetes Cluster (Terraform)
Week 3 → Deploy Microservices on Kubernetes
Week 4 → Package & Manage Kubernetes Deployment with Helm
```

---

## 📁 Project Structure

```text
devops-internship/
├── week1/
│   ├── backend-service/
│   ├── frontend-service/
│   └── README.md
│
├── week2/
│   ├── main.tf
│   ├── recreate-cluster.sh
│   └── README.md
│
├── week3/
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   └── README.md
│
├── week4/
│   ├── microservices-chart/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   │       ├── configmap.yaml
│   │       ├── secret.yaml
│   │       ├── backend-deployment.yaml
│   │       ├── backend-service.yaml
│   │       ├── frontend-deployment.yaml
│   │       └── frontend-service.yaml
│   │
│   ├── upgrade.sh
│   └── README.md
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
* Helm

---

# 🔹 Week 1 — Dockerized Microservices

## 🧩 Architecture

* Frontend Service → Port 5001
* Backend Service → Port 5002

Flow:

```text
Client → Frontend → Backend → Frontend → Client
```

### 🔗 Service Communication

```python
response = requests.get("http://localhost:5002/info")
```

### 🐳 Docker Setup

#### Build Images

```bash
cd week1/backend-service
docker build -t backend:1.0 .

cd ../frontend-service
docker build -t frontend:1.0 .
```

#### Run Containers

```bash
docker run -d --name backend -p 5002:5002 backend:1.0
docker run -d --name frontend -p 5001:5001 frontend:1.0
```

### ✅ Verification

```bash
curl http://localhost:5002/health
curl http://localhost:5001/backend-info
```

### 🎯 Outcome

* ✔ Built microservices
* ✔ Containerized using Docker
* ✔ Enabled service-to-service communication
* ✔ Improved security using non-root user

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

resource "minikube_cluster" "cluster" {
  driver       = "docker"
  cluster_name = "devops-week2"
  memory       = "2200mb"
  cpus         = 2
}
```

### 🚀 Setup

```bash
cd week2
terraform init
terraform apply
```

### ✅ Verification

```bash
kubectl cluster-info
kubectl get nodes
```

### 🔁 Cluster Reset

```bash
chmod +x recreate-cluster.sh
./recreate-cluster.sh
```

### 🎯 Outcome

* ✔ Provisioned Kubernetes cluster
* ✔ Used Infrastructure as Code
* ✔ Automated cluster lifecycle
* ✔ Resolved real DevOps issues

---

# 🔹 Week 3 — Kubernetes Deployment

## 📌 Overview

Deploy Docker containers into Kubernetes using YAML manifests.

## ⚙️ Components Used

* Deployments → Manage pods
* Services → Enable communication
* ConfigMap → Non-sensitive configuration
* Secret → Sensitive data

## 🔗 Architecture

```text
Frontend Pod → Backend Service → Backend Pods
```

### 🚀 Setup

#### Start Cluster

```bash
minikube start -p devops-week2
```

#### Load Images

```bash
minikube image load backend:1.0 -p devops-week2
minikube image load frontend:1.0 -p devops-week2
```

#### Apply Manifests

```bash
kubectl apply -f week3/
```

### ✅ Verification

```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

### 🔗 Internal Communication Test

```bash
kubectl exec -it <frontend-pod> -- python3 -c "import urllib.request; print(urllib.request.urlopen('http://backend-service:5000/health').read())"
```

### 🎯 Outcome

* ✔ Deployed microservices on Kubernetes
* ✔ Configured Services for communication
* ✔ Used ConfigMap & Secret
* ✔ Implemented health checks
* ✔ Verified inter-service networking

---

# 🔹 Week 4 — Helm Deployment & Management

## 📌 Overview

Week 4 converts the Week 3 raw Kubernetes manifests into a **single reusable Helm chart**.

Instead of applying multiple YAML files individually, Helm packages the application into one chart that can be installed, configured, upgraded, rolled back, and removed as a single release. 

## 📁 Helm Chart Structure

```text
week4/
├── microservices-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── configmap.yaml
│       ├── secret.yaml
│       ├── backend-deployment.yaml
│       ├── backend-service.yaml
│       ├── frontend-deployment.yaml
│       └── frontend-service.yaml
│
├── upgrade.sh
└── README.md
```

## ⚙️ Helm Components

### `Chart.yaml`

Contains chart metadata such as:

* Chart name
* Chart version
* Application version

### `values.yaml`

Contains configurable application settings, including:

* Image repository and tag
* Image pull policy
* Replica counts
* Ports
* CPU and memory resources
* Health probe settings
* ConfigMap values
* Secret value
* Service type

### `templates/`

Contains the Kubernetes manifests from Week 3 rewritten as Helm templates using Go template placeholders such as:

```text
{{ .Values.xxx }}
```

This allows configuration to be changed through `values.yaml` instead of modifying each Kubernetes YAML file directly. 

---

## 🚀 Helm Setup

### 1. Start the Kubernetes Cluster

```bash
minikube start -p devops-week2
```

### 2. Load Docker Images

```bash
minikube image load backend:1.0 -p devops-week2
minikube image load frontend:1.0 -p devops-week2
```

### 3. Install the Helm Chart

```bash
cd week4
helm install microservices ./microservices-chart
```

This creates a Helm release named `microservices`. 

---

## ✅ Verify Helm Deployment

```bash
helm list
kubectl get pods
kubectl get deployments
kubectl get services
```

The Week 4 deployment was verified with the microservices running through the Helm release. 

---

## 🔄 Helm Upgrade

An `upgrade.sh` script demonstrates updating the application through Helm.

The upgrade:

* Increases the backend replicas from **2 to 3**
* Changes the log level from `info` to `debug`
* Waits for the rollout to complete
* Displays the Helm release status
* Verifies the resulting pods

Run:

```bash
chmod +x upgrade.sh
./upgrade.sh
```

The upgrade was verified through Helm history and Kubernetes pod status, with **3 backend replicas running**. 

---

## ↩️ Helm Rollback

Helm provides release history and rollback functionality.

View release history:

```bash
helm history microservices
```

Rollback to the previous revision:

```bash
helm rollback microservices 1
```

This allows an earlier version of the deployment to be restored if an upgrade causes a problem. 

---

## 🗑️ Uninstall Helm Release

The complete application can be removed using:

```bash
helm uninstall microservices
```

This removes the resources managed by the Helm release. 

---

## 🛠️ Issues Faced & Troubleshooting

### 1. Docker Desktop Not Running

`minikube start` failed because the cluster uses Docker as its driver.

**Solution:** Started Docker Desktop, confirmed WSL2 integration, and restarted Minikube successfully. 

### 2. Helm Installation Failed Because Resources Already Existed

Helm installation initially failed because the Kubernetes resources created during Week 3 were still present.

Helm could not automatically adopt those existing resources into the new release.

**Solution:** Deleted the old Week 3 resources, verified the cluster was clean, and then installed the Helm chart successfully. 

---

## 🎯 Week 4 Outcome

* ✔ Converted Week 3 Kubernetes manifests into Helm templates
* ✔ Created a reusable Helm chart
* ✔ Centralized configuration in `values.yaml`
* ✔ Installed the microservices as a single Helm release
* ✔ Verified Kubernetes resources through Helm
* ✔ Performed a Helm upgrade
* ✔ Increased backend replicas from 2 to 3
* ✔ Verified Helm release history
* ✔ Demonstrated Helm rollback capability
* ✔ Documented troubleshooting and deployment issues 

---

# 💡 Key Learnings

* **Docker** → Application packaging
* **Kubernetes** → Container orchestration
* **Terraform** → Infrastructure automation
* **Services** → Stable communication layer
* **Probes** → Health monitoring and self-healing
* **Helm** → Kubernetes application packaging and release management
* **values.yaml** → Centralized configuration
* **Helm upgrade** → Application version/configuration updates
* **Helm rollback** → Recovery to a previous release version

---

# 📌 Final Conclusion

This project demonstrates a complete DevOps workflow:

```text
Build
  ↓
Containerize
  ↓
Provision
  ↓
Deploy
  ↓
Package
  ↓
Upgrade / Rollback
  ↓
Verify
```

The four weeks build on each other:

```text
Week 1
Python Flask + Docker
        ↓
Week 2
Terraform + Minikube Kubernetes Cluster
        ↓
Week 3
Kubernetes Deployments + Services + ConfigMap + Secret
        ↓
Week 4
Helm Chart + Release Management
```

---

# 🚀 Future Improvements

* Add Ingress Controller
* Implement CI/CD using GitHub Actions
* Deploy to Cloud (AWS / Azure / GCP)
* Add Monitoring using Prometheus + Grafana
* Add centralized logging
* Implement automated testing
* Add production-ready security practices

---

## ⭐ If you like this project, give it a star!
