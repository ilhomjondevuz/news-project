# 📰 News Website

A Django-based news website built with Python and Django. The platform allows users to read news articles, browse categories, and explore the latest updates.

## 🚀 Features

- News article management
- News categories
- Article details page
- Image uploads for news articles
- Responsive web design
- Django Admin panel
- PostgreSQL database
- Environment variable configuration

## 🛠️ Technologies

- Python 3
- Django
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Git & GitHub

## 📁 Project Structure

```text
newsProject/
│
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── newsApp/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── media/
│
├── static/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

*Note: The project structure may vary depending on the application configuration.*

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/newsProject.git
```

```bash
cd newsProject
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Configure your database credentials and Django settings inside `.env`.

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database

This project uses PostgreSQL as its primary database.

Default PostgreSQL port:

```text
5432
```

Configure database credentials through environment variables.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| SECRET_KEY | Django secret key |
| DEBUG | Debug mode |
| ALLOWED_HOSTS | Allowed hostnames |
| DB_NAME | Database name |
| DB_USER | Database username |
| DB_PASSWORD | Database password |
| DB_HOST | Database host |
| DB_PORT | Database port |

## 📸 Screenshots

Screenshots of the website will be added here.

## 👨‍💻 Author

**Ilhomjon**

Python Backend Developer

- GitHub: [ilhomjondevuz](https://github.com/ilhomjondevuz)

## 📄 License

This project is developed for educational and portfolio purposes.
