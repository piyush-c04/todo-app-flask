# 📝 ToDo App (Flask + Docker)

A simple yet functional ToDo web application built with **Flask**, styled using **HTML/CSS**, and packaged using **Docker** for easy deployment and portability.

---
![Screenshot (290)](https://github.com/user-attachments/assets/184e72f5-8a49-494b-a7b1-ca5814226ec6)


## 🚀 Features

* ✅ Add, delete, and manage ToDo tasks
* 📓 SQLite-based persistent storage
* 🐳 Dockerized for easy containerized deployment
* ♻️ Modular structure using Flask application factory

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
| Containerization       | Docker                 |
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
├── .env                    # Env config (not committed)
├── .gitignore              # Git ignored files
└── README.md               # You're here
```

---

## ⚙️ Environment Setup

### 📌 Prerequisites

* [Python 3.11+](https://www.python.org/)
* [Docker](https://www.docker.com/)
* Git
---
## Docker Image Building and Containerization:
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

## 📦 ToDo for Future Versions

* [ ] Add user authentication
* [ ] Deploy with Gunicorn & Nginx
* [ ] Add PostgreSQL & Docker Compose
* [ ] Add CI/CD with GitHub Actions

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, create a feature branch, and open a pull request.

