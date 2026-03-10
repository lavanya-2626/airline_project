from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.flights.models import Flight
from apps.bookings.models import Booking
from apps.users.models import UserProfile
from apps.notifications.models import Notification
from datetime import datetime, timedelta
import uuid
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample flights, users, and bookings.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting DB seeding...'))
        
        # 1. Create Flights
        self.stdout.write('Creating flights...')
        flights_data = [
            {
                'flight_id': 'AX101',
                'airline_name': 'SkyBound Airways',
                'source': 'London (LHR)',
                'destination': 'New York (JFK)',
                'price': 450.00,
                'seats_total': 200,
                'seats_available': 180,
                'aircraft_type': 'Boeing 737',
            },
            {
                'flight_id': 'AX202',
                'airline_name': 'Horizon Air',
                'source': 'Paris (CDG)',
                'destination': 'Tokyo (NRT)',
                'price': 850.00,
                'seats_total': 300,
                'seats_available': 150,
                'aircraft_type': 'Airbus A380',
            },
            {
                'flight_id': 'AX303',
                'airline_name': 'Oceanic Global',
                'source': 'Dubai (DXB)',
                'destination': 'Singapore (SIN)',
                'price': 320.00,
                'seats_total': 180,
                'seats_available': 45,
                'aircraft_type': 'Boeing 737',
            },
            {
                'flight_id': 'AX404',
                'airline_name': 'SkyBound Airways',
                'source': 'Berlin (BER)',
                'destination': 'Sydney (SYD)',
                'price': 1200.00,
                'seats_total': 250,
                'seats_available': 200,
                'aircraft_type': 'Boeing 747',
            },
            {
                'flight_id': 'AX505',
                'airline_name': 'Vista Jet',
                'source': 'Mumbai (BOM)',
                'destination': 'Paris (CDG)',
                'price': 600.00,
                'seats_total': 150,
                'seats_available': 10,
                'aircraft_type': 'Airbus A320',
            }
        ]

        created_flights = []
        for f_data in flights_data:
            flight, created = Flight.objects.get_or_create(
                flight_id=f_data['flight_id'],
                defaults={
                    **f_data,
                    'departure_time': datetime.now() + timedelta(days=random.randint(1, 10), hours=random.randint(1, 23)),
                    'arrival_time': datetime.now() + timedelta(days=random.randint(1, 10), hours=random.randint(24, 48)),
                }
            )
            created_flights.append(flight)
            if created:
                self.stdout.write(f'  Created flight {flight.flight_id}')

        # 2. Create Users
        self.stdout.write('Creating users...')
        users = [
            ('demo_user', 'demo@example.com', 'Demo@12345'),
            ('admin', 'admin@example.com', 'Admin@12345'),
        ]
        
        for username, email, password in users:
            if not User.objects.filter(username=username).exists():
                if username == 'admin':
                    user = User.objects.create_superuser(username, email, password)
                else:
                    user = User.objects.create_user(username, email, password)
                
                # Profile is automatically created via signal if implemented, 
                # but let's ensure it exists
                UserProfile.objects.get_or_create(user=user, defaults={
                    'nationality': 'Indian',
                    'city': 'Mumbai',
                    'country': 'India'
                })
                self.stdout.write(f'  Created user {username}')

        # 3. Create sample bookings for demo_user
        self.stdout.write('Creating bookings...')
        demo_user = User.objects.get(username='demo_user')
        if not Booking.objects.filter(user=demo_user).exists():
            for i in range(2):
                flight = created_flights[i % len(created_flights)]
                booking = Booking.objects.create(
                    booking_id=f"BK-{uuid.uuid4().hex[:8].upper()}",
                    user=demo_user,
                    flight=flight,
                    passenger_name="Demo Traveler",
                    passenger_email=demo_user.email,
                    passenger_phone="+91 9999999999",
                    seat_number=f"{random.randint(1, 30)}{random.choice('ABCDEF')}",
                    status='confirmed',
                    payment_status='paid',
                    total_price=flight.price,
                )
                self.stdout.write(f'  Created booking {booking.booking_id} for {flight.flight_id}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
