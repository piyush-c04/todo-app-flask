# 📝 ToDo App (Flask + Docker + Deployment on Kubernetes)

A simple yet functional ToDo web application built with **Flask**, styled using **HTML/CSS**, and packaged using **Docker** for easy deployment and portability ,Deployed for scalability via **Kubernetes**.

---
![Screenshot (290)](https://github.com/user-attachments/assets/184e72f5-8a49-494b-a7b1-ca5814226ec6)


## 🚀 Features

* ✅ Add, delete, and manage ToDo tasks
* 📓 SQLite-based persistent storage
* 🐳 Dockerized for easy containerized deployment
* ♻️ Modular structure using Flask application factory
* ⎈️ Supports full Kubernetes deployment

-
![Screenshot (292)](https://github.com/user-attachments/assets/7fb0f0b2-a051-454f-830b-76ca8462015b)
--
![Screenshot (295)](https://github.com/user-attachments/assets/1b1b0e8b-72f1-4361-b7bb-8f9a902fe78d)
---
![Screenshot (296)](https://github.com/user-attachments/assets/8a6c4119-7cd8-4431-8e84-82d8018e578a)
----
![Screenshot (288)](https://github.com/user-attachments/assets/8783e6dd-7687-4719-8411-e292f2fd0ec2)


## 📦 Version

> **Current Version:** `v1.0.0`

---

## 💪 Technologies Used

| Layer                  | Tool/Tech              |
| ---------------------- | ---------------------- |
| Backend                | Python 3.11, Flask     |
| Frontend               | HTML, CSS              |
| Database               | SQLite                 |
| Containerization       | Docker, Kubernetes     |
| Environment Management | Python `venv` + `.env` |

---

## 📁 Project Structure

```
todo-app-flask/
│
├── app/                    # Flask app package
│   ├── __init__.py         # App factory
│   ├── models.py           # SQLAlchemy models
│   └── routes.py           # Routes and views
│
├── templates/              # HTML templates
├── static/                 # CSS & assets
│
├── run.py                  # App entry point
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
├── configmap.yaml          # Kuberenetes: to store application-specific configurations
├── deployment.yaml         # Manage replicated Pods, providing declarative updates and rollbacks
├── services.yaml           # Expose your applications running in Pods to the network
├── .env                    # Env config (not committed)
├── .gitignore              # Git ignored files
└── README.md               # You're here
```

---

## ⚙️ Environment Setup

### 📌 Prerequisites

* [Python 3.11+](https://www.python.org/)
* [Docker](https://www.docker.com/)
* [Minikube or Kubernetes cluster](https://minikube.sigs.k8s.io/docs/start/)
* Git

---

## 📦 Docker Image Building and Containerization:
![Screenshot (300)](https://github.com/user-attachments/assets/3cd18791-7233-43d4-89d7-49e8d506484c)
--
![Screenshot (301)](https://github.com/user-attachments/assets/2ddbf323-7e14-42be-89cf-b7b4b54b5a1a)

---

## 💻 Local Development (without Docker)

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python run.py

# 4. Open in browser
http://localhost:5000
```

---

## 🐳 Docker Usage

### 🏗️ Build Docker Image

```bash
docker build -t todo-flask-app .
```

### 🚀 Run Container

```bash
docker run -p 5000:5000 --env-file .env todo-flask-app
```

---

## ⎈️ Kubernetes Deployment (Full Container Orchestration)

This project fully supports running on a **Kubernetes cluster**, enabling horizontal scaling, declarative infrastructure, and production-grade orchestration.

### 🧾 Required Manifests:
- `configmap.yaml` — Stores environment variables
- `deployment.yaml` — Deploys Flask app as a containerized pod
- `service.yaml` — Exposes the app via NodePort

### 🚀 Deploy Steps:
![Screenshot (305)](https://github.com/user-attachments/assets/95aa8a97-e485-4cc0-a668-bbea903b8f94)
![Screenshot (306)](https://github.com/user-attachments/assets/c125efab-7616-4af8-967a-c852005ef830)
![Screenshot (307)](https://github.com/user-attachments/assets/f7836003-073f-4c55-a525-ece4fd91658e)

```bash
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 🌐 Access Options:
![Screenshot (309)](https://github.com/user-attachments/assets/b93a2718-1002-4a4f-bc83-ca7e4393e6ab)
![Screenshot (310)](https://github.com/user-attachments/assets/d79ff513-a766-495b-ae34-10c5cb891e81)

- Recommended: 
  ```bash
  minikube service todo-app-service
  ```
- Alternate:
  ```bash
  minikube tunnel   # Then open http://localhost:30007
  ```
- Temporary dev access:
  ```bash
  kubectl port-forward service/todo-app-service 5000:5000
  ```

> ⚠️ Note: SQLite is ephemeral in Kubernetes. For persistent or multi-replica setups, consider PostgreSQL with Persistent Volumes or StatefulSets.
![Screenshot (311)](https://github.com/user-attachments/assets/07bf51f1-b062-4e20-9995-6005e2be4198)

---

## 📦 ToDo for Future Versions

* [ ] Add user authentication
* [ ] Deploy with Gunicorn & Nginx
* [ ] Add PostgreSQL & Docker Compose
* [ ] Add CI/CD with GitHub Actions / Jenkins
* [ ] Add Persistent Volume or PostgreSQL for Kubernetes

(SRC @master branch)
---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, create a feature branch, and open a pull request.
