# Airline Ticket Booking System - Django Project

## Overview
This is a Django-based web application for booking airline tickets online. Users can search flights, book tickets, and manage their reservations.

## Features

- **User Authentication**: Registration, Login, Logout
- **Flight Search**: Search flights by source, destination, and travel date
- **Flight Booking**: Book tickets with passenger details
- **Booking Management**: View booking history and booking details
- **User Profile**: Manage user information
- **Admin Panel**: Manage flights, bookings, and users

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

## Installation

### 1. Clone or navigate to the project directory
```bash
cd airline_project
```

### 2. Create a virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```

### 6. Collect static files
```bash
python manage.py collectstatic
```

### 7. Run the development server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
airline_project/
├── airline_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── flights/                  # Main app
│   ├── models.py            # Database models
│   ├── views.py             # Views
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin configuration
│   └── __init__.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── search_flight.html
│   ├── booking.html
│   ├── login.html
│   ├── register.html
│   ├── booking_confirmation.html
│   ├── booking_history.html
│   └── profile.html
├── static/                  # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── manage.py
├── requirements.txt
└── db.sqlite3               # Database (created after migrations)
```

## Database Models

### 1. User (Django built-in)
- username
- email
- password

### 2. UserProfile
- user (OneToOne to User)
- phone
- date_of_birth
- profile_picture

### 3. Flight
- flight_id
- airline_name
- source
- destination
- departure_time
- arrival_time
- price
- seats_available

### 4. Booking
- booking_id
- user (ForeignKey to User)
- flight (ForeignKey to Flight)
- passenger_name
- booking_date
- seat_number
- status (pending/confirmed/cancelled)
- passenger_email
- passenger_phone

## Available URLs

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/search/` | Search flights |
| `/book/<flight_id>/` | Book a flight |
| `/booking-confirmation/<booking_id>/` | Booking confirmation |
| `/booking-history/` | View booking history |
| `/register/` | User registration |
| `/login/` | User login |
| `/logout/` | User logout |
| `/profile/` | User profile |
| `/admin/` | Admin panel |

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`

### Admin Features:
- Add, edit, delete flights
- View and manage bookings
- Filter flights by airline, route, and date
- Search bookings by ID or passenger name
- Manage user profiles

## Usage

### 1. Register a new account
- Click on "Register" in the navbar
- Fill in username, email, and password
- Click "Register"

### 2. Search flights
- Go to "Search Flights" or use the search form on home page
- Enter departure city, arrival city, and travel date
- Click "Search"

### 3. Book a flight
- Click "Book Now" on a flight
- Fill in passenger details
- Enter seat number
- Click "Confirm Booking"

### 4. View booking history
- Click on "My Bookings" in the navbar
- See all your past bookings

### 5. Add flights (Admin only)
- Log in with admin account
- Go to Admin Panel
- Click on "Flights" and add new flights

## Future Enhancements

- [ ] Payment Gateway Integration
- [ ] Email Notifications
- [ ] Flight Cancellation Feature
- [ ] Seat Selection System
- [ ] Mobile Responsive Improvements
- [ ] Flight Status Updates
- [ ] Rating and Reviews
- [ ] Multi-language Support
- [ ] Two-Factor Authentication

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'django'`
- **Solution**: Make sure you've activated the virtual environment and installed requirements

**Issue**: `No such table: flights_flight`
- **Solution**: Run migrations: `python manage.py migrate`

**Issue**: Static files not loading
- **Solution**: Run `python manage.py collectstatic`

## License
This project is open source and available under the MIT License.

## Support
For issues and questions, please refer to Django documentation: https://docs.djangoproject.com/

## Contact
For more information, contact the development team.

---

**Last Updated**: March 2026
**Version**: 1.0
