# 🚀 DevOps Internship Project

## Dockerized Microservices → Kubernetes → Terraform

---

## 📌 Project Overview

This repository showcases a complete **3-week DevOps learning journey**, where a microservices application is:

- Built using Python (Flask)
- Containerized using Docker
- Deployed on Kubernetes
- Provisioned using Terraform (Infrastructure as Code)

---

## 🧠 Project Flow

```text
Week 1 → Build & Dockerize Microservices
Week 2 → Provision Kubernetes Cluster (Terraform)
Week 3 → Deploy Microservices on Kubernetes

📁 Project Structure
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
└── README.md
🛠️ Technologies Used
Python 3.12
Flask
Requests
Docker
Kubernetes (Minikube)
Terraform
kubectl
🔹 Week 1 — Dockerized Microservices
🧩 Architecture
Frontend Service → Port 5001
Backend Service → Port 5002
Client → Frontend → Backend → Frontend → Client
🔗 Service Communication
response = requests.get("http://localhost:5002/info")
🐳 Docker Setup
Build Images
cd week1/backend-service
docker build -t backend:1.0 .

cd ../frontend-service
docker build -t frontend:1.0 .
Run Containers
docker run -d --name backend -p 5002:5002 backend:1.0
docker run -d --name frontend -p 5001:5001 frontend:1.0
✅ Verification
curl http://localhost:5002/health
curl http://localhost:5001/backend-info
🎯 Week 1 Outcome

✔ Built microservices
✔ Containerized using Docker
✔ Enabled service-to-service communication
✔ Improved security using non-root user

🔹 Week 2 — Kubernetes with Terraform
⚙️ Terraform Configuration
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
🚀 Setup
cd week2
terraform init
terraform apply
✅ Verification
kubectl cluster-info
kubectl get nodes
🔁 Cluster Reset
chmod +x recreate-cluster.sh
./recreate-cluster.sh
🎯 Week 2 Outcome

✔ Provisioned Kubernetes cluster
✔ Used Infrastructure as Code
✔ Automated cluster lifecycle
✔ Resolved real DevOps issues

🔹 Week 3 — Kubernetes Deployment
📌 Overview

In this phase, Docker containers from Week 1 are deployed into the Kubernetes cluster created in Week 2 using raw YAML manifests.

⚙️ Components Used
Deployments → Manage pods
Services → Enable communication
ConfigMap → Non-sensitive config
Secret → Sensitive data
🔗 Architecture
Frontend Pod → Backend Service → Backend Pods
🚀 Setup
Start Cluster
minikube start -p devops-week2
Load Images
minikube image load backend:1.0 -p devops-week2
minikube image load frontend:1.0 -p devops-week2
Apply Manifests
kubectl apply -f week3/
✅ Verification
kubectl get pods
kubectl get services
kubectl get deployments
🔗 Internal Communication Test
kubectl exec -it <frontend-pod> -- python3 -c "import urllib.request; print(urllib.request.urlopen('http://backend-service:5000/health').read())"
🎯 Week 3 Outcome

✔ Deployed microservices on Kubernetes
✔ Configured Services for communication
✔ Used ConfigMap & Secret
✔ Implemented health checks (liveness/readiness)
✔ Verified inter-service networking

💡 Key Learnings
Docker → Application packaging
Kubernetes → Container orchestration
Terraform → Infrastructure automation
Services → Stable communication layer
Probes → Self-healing systems
📌 Final Conclusion

This project demonstrates a complete DevOps pipeline:

👉 Build → Containerize → Provision → Deploy → Verify

It forms a strong foundation for:

CI/CD pipelines
Cloud deployments (AWS/GCP/Azure)
Scalable microservices systems
🚀 Future Improvements
Add Ingress Controller (access via browser)
Implement CI/CD (GitHub Actions)
Use Helm charts
Deploy to cloud (AWS / Azure / GCP)
Add monitoring (Prometheus + Grafana)

---

## 🔥 What improved in your version

- ✅ Added **Week 3 (missing before)**
- ✅ Fixed naming consistency (`backend:1.0`)
- ✅ Cleaner structure (more recruiter-friendly)
- ✅ Better flow (storytelling of DevOps pipeline)
- ✅ More professional tone

---

If you want next level 🔥  
I can help you:
- write **LinkedIn post for this project**
- prepare **interview questions from this repo**
- or upgrade this to **production-level DevOps project** 🚀


