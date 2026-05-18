# FastAPI Backend System Design

A production-style backend application built using FastAPI to demonstrate modern backend system design concepts including async APIs, middleware, routing, and dependency injection.

---

## Features

- FastAPI backend architecture
- Async API endpoints
- Modular routing system
- Middleware request logging
- Dependency Injection
- Swagger API Documentation
- Clean production-style folder structure
- GitHub version-controlled project

---

## Project Structure

```plaintext
fastapi-backend-system-design/
│
├── app/
│   ├── api/
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── middleware/
│   │   └── logger.py
│   │
│   ├── dependencies/
│   │   └── auth.py
│   │
│   ├── schemas/
│   │   └── user.py
│   │
│   └── main.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## Installation

Clone repository

```bash
git clone https://github.com/kolurash/fastapi-backend-system-design.git
cd fastapi-backend-system-design
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
.\venv\Scripts\Activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
uvicorn app.main:app --reload
```

Server runs at:

```plaintext
http://127.0.0.1:8000
```

---

## API Documentation

Swagger Docs:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Implemented Concepts

### Async APIs
Efficient non-blocking request handling using async and await.

### Middleware
Logs incoming requests for monitoring and debugging.

### Routing
Modular route separation for scalability.

### Dependency Injection
Reusable backend authentication verification.

---

## Sample API Response

```json
{
  "status": "verified",
  "users": [
    {
      "id": 1,
      "name": "Bangaram"
    },
    {
      "id": 2,
      "name": "Developer"
    }
  ]
}
```

---

## Learning Outcomes

- FastAPI project structure
- Production backend design
- Async programming
- API documentation
- Modular architecture
- Version control using Git and GitHub

---

## Author

Rashmitha
Prompt Engineering Intern
