"""
Professional Airline Booking System - Setup Sample Data
Run: python manage.py shell < setup_sample_data.py
"""

from flights.models import Flight, Booking, UserProfile, Review, Notification
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import uuid


def create_sample_airlines():
    """Create sample flight data with professional details"""
    
    flights_data = [
        {
            'flight_id': 'AA101',
            'airline_name': 'American Airlines',
            'source': 'New York (JFK)',
            'destination': 'Los Angeles (LAX)',
            'departure_time': datetime.now() + timedelta(days=7, hours=8),
            'arrival_time': datetime.now() + timedelta(days=7, hours=16),
            'price': 299.99,
            'seats_total': 200,
            'seats_available': 145,
            'aircraft_type': 'Boeing 737',
            'is_active': True,
        },
        {
            'flight_id': 'UA202',
            'airline_name': 'United Airlines',
            'source': 'Chicago (ORD)',
            'destination': 'Miami (MIA)',
            'departure_time': datetime.now() + timedelta(days=5, hours=10),
            'arrival_time': datetime.now() + timedelta(days=5, hours=14),
            'price': 199.99,
            'seats_total': 180,
            'seats_available': 95,
            'aircraft_type': 'Airbus A320',
            'is_active': True,
        },
        {
            'flight_id': 'DL303',
            'airline_name': 'Delta Airlines',
            'source': 'Atlanta (ATL)',
            'destination': 'Boston (BOS)',
            'departure_time': datetime.now() + timedelta(days=3, hours=6),
            'arrival_time': datetime.now() + timedelta(days=3, hours=10),
            'price': 159.99,
            'seats_total': 156,
            'seats_available': 78,
            'aircraft_type': 'Boeing 737',
            'is_active': True,
        },
        {
            'flight_id': 'SW404',
            'airline_name': 'Southwest Airlines',
            'source': 'San Francisco (SFO)',
            'destination': 'Dallas (DFW)',
            'departure_time': datetime.now() + timedelta(days=4, hours=9),
            'arrival_time': datetime.now() + timedelta(days=4, hours=15),
            'price': 219.99,
            'seats_total': 150,
            'seats_available': 62,
            'aircraft_type': 'Boeing 737',
            'is_active': True,
        },
        {
            'flight_id': 'BA505',
            'airline_name': 'British Airways',
            'source': 'London (LHR)',
            'destination': 'New York (JFK)',
            'departure_time': datetime.now() + timedelta(days=10, hours=18),
            'arrival_time': datetime.now() + timedelta(days=11, hours=4),
            'price': 549.99,
            'seats_total': 256,
            'seats_available': 120,
            'aircraft_type': 'Boeing 747',
            'is_active': True,
        },
        {
            'flight_id': 'AF606',
            'airline_name': 'Air France',
            'source': 'Paris (CDG)',
            'destination': 'Tokyo (NRT)',
            'departure_time': datetime.now() + timedelta(days=6, hours=20),
            'arrival_time': datetime.now() + timedelta(days=7, hours=14),
            'price': 799.99,
            'seats_total': 350,
            'seats_available': 180,
            'aircraft_type': 'Airbus A380',
            'is_active': True,
        },
    ]
    
    for flight_data in flights_data:
        flight, created = Flight.objects.get_or_create(
            flight_id=flight_data['flight_id'],
            defaults=flight_data
        )
        status = "✓ Created" if created else "• Exists"
        print(f"{status}: {flight.flight_id} - {flight.airline_name}")


def create_sample_users():
    """Create professional sample users"""
    
    users_data = [
        {
            'username': 'demo_user',
            'email': 'demo@example.com',
            'password': 'Demo@12345',
            'first_name': 'Demo',
            'last_name': 'User',
        },
        {
            'username': 'john_doe',
            'email': 'john.doe@example.com',
            'password': 'John@12345',
            'first_name': 'John',
            'last_name': 'Doe',
        },
        {
            'username': 'jane_smith',
            'email': 'jane.smith@example.com',
            'password': 'Jane@12345',
            'first_name': 'Jane',
            'last_name': 'Smith',
        },
    ]
    
    for user_data in users_data:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
            )
            UserProfile.objects.create(
                user=user,
                phone='+1-555-0100',
                country='United States',
                nationality='American',
            )
            print(f"✓ Created user: {user_data['username']}")
        else:
            print(f"• User exists: {user_data['username']}")


def create_admin_user():
    """Create admin superuser"""
    
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='Admin@12345',
            first_name='Admin',
            last_name='User',
        )
        UserProfile.objects.create(
            user=admin,
            phone='+1-555-0101',
            country='United States',
            nationality='American',
        )
        print("✓ Created superuser: admin")
    else:
        print("• Admin user exists")


def create_sample_bookings():
    """Create professional sample bookings"""
    
    demo_user = User.objects.filter(username='demo_user').first()
    if not demo_user:
        print("! Demo user not found, skipping bookings")
        return
    
    flights = Flight.objects.all()[:3]
    seats = ['12A', '12B', '15C']
    
    for i, flight in enumerate(flights):
        session_count = Booking.objects.filter(flight=flight).count()
        if session_count == 0:
            booking_id = f"BK-{uuid.uuid4().hex[:8].upper()}"
            
            booking = Booking.objects.create(
                booking_id=booking_id,
                user=demo_user,
                flight=flight,
                passenger_name=f'John Traveler {i+1}',
                passenger_email='traveler@example.com',
                passenger_phone='+1-555-0102',
                seat_number=seats[i],
                status='confirmed',
                payment_status='paid',
                total_price=flight.price,
                nationality='American',
            )
            
            # Update seats
            flight.seats_available -= 1
            flight.save()
            
            print(f"✓ Created booking: {booking_id}")
        else:
            print(f"• Booking exists for flight: {flight.flight_id}")


if __name__ == '__main__':
    print("\n" + "="*60)
    print("PROFESSIONAL AIRLINE BOOKING SYSTEM - SETUP")
    print("="*60 + "\n")
    
    print("Creating sample flights...")
    create_sample_airlines()
    
    print("\nCreating sample users...")
    create_sample_users()
    
    print("\nCreating admin user...")
    create_admin_user()
    
    print("\nCreating sample bookings...")
    create_sample_bookings()
    
    print("\n" + "="*60)
    print("✓ SETUP COMPLETE")
    print("="*60)
    print("\n📋 CREDENTIALS:")
    print("─" * 60)
    print("Admin    | Username: admin        | Password: Admin@12345")
    print("Demo     | Username: demo_user    | Password: Demo@12345")
    print("User 1   | Username: john_doe     | Password: John@12345")
    print("User 2   | Username: jane_smith   | Password: Jane@12345")
    print("─" * 60 + "\n")
