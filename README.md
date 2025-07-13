# Project Management API

A secure REST API built with Django REST Framework and JWT authentication.

## 🚀 Features

- JWT Authentication (Access & Refresh tokens)
- User registration (no token required)
- CRUD operations for projects, tasks, and comments
- Token refresh mechanism
- Docker support

## 🔧 Setup

### Requirements
- Python 3.9+
- PostgreSQL
- Docker (optional)

### Installation
1. Clone repo & create virtualenv:
```bash
git clone https://github.com/LokeshWakode12/project-management-api.git
cd project-management-api
python -m venv venv
source venv/bin/activate


pip install -r requirements.txt
cp .env.example .env  # Update with your settings
python manage.py migrate
python manage.py runserver
docker-compose up -d --build

POST /api/register/
{
  "username": "newuser",
  "email": "user@example.com",
  "password": "yourpassword123"
}

POST /api/token/
{
  "username": "newuser",
  "password": "yourpassword123"
}

GET /api/projects/
Headers: Authorization: Bearer <access_token>


POST /api/token/refresh/
{
  "refresh": "<your_refresh_token>"
}

## Accept register and token API each api is binded with auth token
