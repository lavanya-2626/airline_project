# 🛫 Professional Airline E-Commerce Booking System

## Overview

A **production-ready Django web application** for airline ticket booking with comprehensive features including flight search, real-time booking, payment tracking, and professional admin management.

**Edition:** Professional v2.0  
**Status:** ✅ Production Ready  
**Framework:** Django 4.2.8  
**Database:** SQLite3 (PostgreSQL ready)  
**Python:** 3.8+

---

## 🌟 Features

### ✨ Core Features
- 🔐 Secure user authentication & authorization
- ✈️ Real-time flight search & filtering
- 🎫 One-click flight booking
- 💳 Payment tracking & management
- 📱 Responsive mobile-friendly design
- 📧 Email notifications (framework ready)
- ⭐ Flight reviews & ratings system
- 👤 Comprehensive user profiles

### 🚀 Advanced Features
- Aircraft type information (Boeing 737/747, Airbus A320/A380)
- Dynamic seat availability tracking
- Booking status management
- Payment status workflows
- Passenger passport information capture
- Promotional notification system
- Review moderation framework

### 👨‍💼 Admin Features
- Advanced flight management dashboard
- Booking administration & monitoring
- User profile management
- Review management
- Notification broadcasting
- Analytics-ready database structure

---

## 🏗️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | Django 4.2.8 |
| Database | SQLite3 / PostgreSQL |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Authentication | Django Auth |
| Forms | Django Forms |
| Admin | Django Admin Interface |

---

## 📦 Quick Start

### Prerequisites
```
Python 3.8+
pip
Virtual Environment (recommended)
```

### Installation (5 minutes)

**1. Setup Environment**
```bash
cd airline_project
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Apply Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Create Admin Account**
```bash
python manage.py createsuperuser
```

**5. Load Sample Data (Optional)**
```bash
python manage.py shell < setup_sample_data.py
```

**6. Run Development Server**
```bash
python manage.py runserver
```

**Access:** 🌐 http://127.0.0.1:8000/

---

## 👤 Default Credentials

| User Type | Username | Password | Role |
|-----------|----------|----------|------|
| Admin | admin | Admin@12345 | Superuser |
| Demo | demo_user | Demo@12345 | Regular User |
| User 1 | john_doe | John@12345 | Regular User |
| User 2 | jane_smith | Jane@12345 | Regular User |

---

## 📋 Main Features & URLs

### User Features
| Feature | URL | Access |
|---------|-----|--------|
| Browse Flights | `/` | Public |
| Search Flights | `/search/` | Public |
| User Registration | `/register/` | Public |
| User Login | `/login/` | Public |
| Book Flight | `/book/<id>/` | Members |
| Booking Confirmation | `/booking-confirmation/<id>/` | Members |
| Booking History | `/booking-history/` | Members |
| User Profile | `/profile/` | Members |
| Logout | `/logout/` | Members |

### Admin Features
| Feature | URL |
|---------|-----|
| Admin Dashboard | `/admin/` |
| Manage Flights | `/admin/flights/flight/` |
| Manage Bookings | `/admin/flights/booking/` |
| Manage Reviews | `/admin/flights/review/` |
| Manage Users | `/admin/auth/user/` |
| Manage Notifications | `/admin/flights/notification/` |

---

## 🔐 Security Features

✅ **Implemented:**
- CSRF token protection on all forms
- Password hashing using Django's auth system
- SQL injection prevention (ORM)
- XSS protection (template escaping)
- User authentication & authorization
- Session management
- Input validation & sanitization

🔆 **Ready for Implementation:**
- Two-factor authentication
- API authentication tokens
- Rate limiting
- CORS configuration
- HTTPS/SSL support

---

## 📁 Project Structure

```
airline_project/
├── airline_project/           # Django project settings
│   ├── settings.py           # Configuration
│   ├── urls.py               # URL routing
│   ├── wsgi.py & asgi.py     # Application entry
│   └── __init__.py
├── flights/                   # Main application
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py               # URL patterns
│   ├── admin.py              # Admin interface
│   ├── apps.py               # App configuration
│   ├── migrations/           # Database migrations
│   └── tests.py              # Unit tests
├── templates/                # HTML templates (8 files)
├── static/                   # Static files (CSS, JS)
├── manage.py                 # Django management CLI
├── setup_sample_data.py      # Sample data setup
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables
├── .gitignore                # Git ignore file
├── README.md                 # This file
├── DOCUMENTATION.md          # Full documentation
└── db.sqlite3                # SQLite database
```

---

## 🚀 Deployment Guide

### Heroku Deployment
```bash
heroku login
heroku create airline-booking-system
git push heroku main
```

### Traditional Server (Nginx + Gunicorn)
```bash
pip install gunicorn
gunicorn airline_project.wsgi:application --bind 0.0.0.0:8000
```

---

## 🛠️ Development Commands

```bash
python manage.py makemigrations        # Create migrations
python manage.py migrate               # Apply migrations
python manage.py createsuperuser       # Create admin
python manage.py runserver             # Run dev server
python manage.py test flights          # Run tests
python manage.py collectstatic         # Collect static files
```

---

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [OWASP Security](https://owasp.org/)

---

## 📄 License

MIT License - Open source and free to use

---

**Status:** ✅ Production Ready | **Version:** 2.0 | **Last Updated:** March 10, 2026

✈️ **Book Your Flights with Confidence!** ✈️
