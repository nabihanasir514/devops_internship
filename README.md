# DevOps Internship - Week 1

## Project Overview

This project contains two Python-based microservices developed using the Flask framework.

- **Frontend Service** (Port **5001**)
- **Backend Service** (Port **5002**)

The frontend service communicates with the backend service using an HTTP GET request to retrieve information from the backend.

---

## Project Structure

```text
devops_internship_week1/
├── backend-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── README.md
```

---

## Technologies Used

- Python 3.12
- Flask
- Requests
- Docker

---

## Microservices

### Backend Service

Runs on **Port 5002**

Available endpoints:

- `GET /health`
- `GET /info`

Example:

```text
http://localhost:5002/info
```

---

### Frontend Service

Runs on **Port 5001**

Available endpoints:

- `GET /health`
- `GET /info`
- `GET /backend-info`

Example:

```text
http://localhost:5001/backend-info
```

---

## Service Communication

The frontend service communicates with the backend service using an HTTP GET request.

Example:

```python
response = requests.get("http://localhost:5002/info")
```

Communication flow:

```text
Client
   │
   ▼
Frontend Service (5001)
   │
HTTP GET /info
   │
   ▼
Backend Service (5002)
   │
Returns JSON Response
   │
   ▼
Frontend Service
   │
   ▼
Client
```

---

## Docker

Each microservice includes a **multi-stage Dockerfile**.

### Features

- Multi-stage build
- Lightweight runtime image
- Runs as a **non-root user**
- Exposes the required application port

---

## Build Docker Images

### Backend

```bash
cd backend-service
docker build -t backend-service:1.0 .
```

### Frontend

```bash
cd frontend-service
docker build -t frontend-service:1.0 .
```

---

## Run Docker Containers

### Backend

```bash
docker run -d --name backend -p 5002:5002 backend-service:1.0
```

### Frontend

```bash
docker run -d --name frontend -p 5001:5001 frontend-service:1.0
```

---

## Verify Running Containers

```bash
docker ps
```

---

## Verify Endpoints

Backend Health

```bash
curl http://localhost:5002/health
```

Backend Info

```bash
curl http://localhost:5002/info
```

Frontend Health

```bash
curl http://localhost:5001/health
```

Frontend Info

```bash
curl http://localhost:5001/info
```

Frontend calling Backend

```bash
curl http://localhost:5001/backend-info
```

---

## Verify Non-Root User

Check the user inside the running containers.

Frontend

```bash
docker exec -it frontend whoami
```

Backend

```bash
docker exec -it backend whoami
```

Expected output:

```text
appuser
```

---

## Outcome

- Developed two independent Python microservices.
- Implemented `/health` and `/info` endpoints.
- Implemented HTTP communication between frontend and backend services.
- Created multi-stage Dockerfiles for both services.
- Configured containers to run as a non-root user.
- Built and tagged Docker images locally.
- Verified successful execution using `docker run`.
