from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse


class Flight(models.Model):
    AIRCRAFT_TYPES = [
        ('Boeing 737', 'Boeing 737'),
        ('Boeing 747', 'Boeing 747'),
        ('Airbus A320', 'Airbus A320'),
        ('Airbus A380', 'Airbus A380'),
    ]
    
    flight_id = models.CharField(max_length=20, unique=True)
    airline_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    seats_total = models.IntegerField(validators=[MinValueValidator(1)])
    seats_available = models.IntegerField(validators=[MinValueValidator(0)])
    aircraft_type = models.CharField(max_length=50, choices=AIRCRAFT_TYPES, default='Boeing 737')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-departure_time']
        verbose_name_plural = 'Flights'
        indexes = [
            models.Index(fields=['flight_id']),
            models.Index(fields=['departure_time']),
        ]

    def __str__(self):
        return f"{self.flight_id} - {self.airline_name} ({self.source} to {self.destination})"
    
    def get_absolute_url(self):
        return reverse('search_flights')
    
    def is_fully_booked(self):
        return self.seats_available == 0
    
    def booking_percentage(self):
        if self.seats_total == 0:
            return 0
        return ((self.seats_total - self.seats_available) / self.seats_total) * 100


class Booking(models.Model):
    BOOKING_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    PAYMENT_STATUS = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded'),
    ]

    booking_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    passenger_phone = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='unpaid')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    
    # Passenger details
    date_of_birth = models.DateField(null=True, blank=True)
    passport_number = models.CharField(max_length=50, blank=True, default='')
    nationality = models.CharField(max_length=100, blank=True, default='')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-booking_date']
        verbose_name_plural = 'Bookings'
        unique_together = ('flight', 'seat_number')
        indexes = [
            models.Index(fields=['booking_id']),
            models.Index(fields=['user']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.booking_id} - {self.passenger_name}"
    
    def get_absolute_url(self):
        return reverse('booking_confirmation', args=[self.id])
    
    def can_cancel(self):
        return self.status in ['pending', 'confirmed']
    
    def get_duration(self):
        return self.flight.arrival_time - self.flight.departure_time


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    passport_number = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    preferred_currency = models.CharField(max_length=3, default='USD')
    newsletter_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return f"Profile of {self.user.username}"
    
    def get_full_address(self):
        parts = [self.address, self.city, self.country, self.zipcode]
        return ', '.join(p for p in parts if p)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reviews')
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(choices=[(i, f'{i} Star') for i in range(1, 6)])
    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'flight')

    def __str__(self):
        return f"Review by {self.user.username} for {self.flight.flight_id}"


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('booking_confirmed', 'Booking Confirmed'),
        ('booking_cancelled', 'Booking Cancelled'),
        ('payment_received', 'Payment Received'),
        ('flight_delayed', 'Flight Delayed'),
        ('promo_offer', 'Promotional Offer'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f"{self.title} - {self.user.username}"
