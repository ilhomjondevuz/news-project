# Django 6.1 Project

A modern Django 6.1 web application built with Python, Django REST Framework, PostgreSQL, and environment-based configuration.

---

## 🚀 Features

- Django 6.1
- Django REST Framework
- PostgreSQL database
- Environment variables with `.env`
- Custom user authentication
- RESTful API
- Swagger / OpenAPI documentation
- Media and static files support
- Internationalization (i18n)
- Uzbek, Russian and English language support
- Django Admin panel
- Production-ready project structure
- Secure configuration using environment variables

---

## 🛠 Tech Stack

| Technology | Version / Usage |
|---|---|
| Python | 3.12+ |
| Django | 6.1 |
| Django REST Framework | Latest compatible version |
| PostgreSQL | 16+ |
| Git | Version control |
| Swagger / OpenAPI | API documentation |

---

## 📁 Project Structure

```text
project/
│
├── apps/
│   ├── accounts/
│   ├── ...
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── locale/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       ├── django.po
│   │       └── django.mo
│   ├── ru/
│   │   └── LC_MESSAGES/
│   │       ├── django.po
│   │       └── django.mo
│   └── uz/
│       └── LC_MESSAGES/
│           ├── django.po
│           └── django.mo
│
├── media/
├── static/
├── templates/
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md