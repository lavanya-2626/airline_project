"""
flights/models.py — Flight and Review domain models.
Business-method helpers (is_fully_booked, booking_percentage) live here
because they are pure domain logic that only depends on model data.
"""
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
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    seats_total = models.IntegerField(validators=[MinValueValidator(1)])
    seats_available = models.IntegerField(validators=[MinValueValidator(0)])
    aircraft_type = models.CharField(
        max_length=50, choices=AIRCRAFT_TYPES, default='Boeing 737'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['departure_time']
        verbose_name_plural = 'Flights'
        indexes = [
            models.Index(fields=['flight_id']),
            models.Index(fields=['departure_time']),
            models.Index(fields=['source', 'destination']),
        ]

    def __str__(self):
        return f"{self.flight_id} — {self.airline_name} ({self.source} → {self.destination})"

    def get_absolute_url(self):
        return reverse('search_flights')

    def is_fully_booked(self):
        return self.seats_available == 0

    def booking_percentage(self):
        if self.seats_total == 0:
            return 0
        return ((self.seats_total - self.seats_available) / self.seats_total) * 100

    def duration(self):
        """Return flight duration as timedelta."""
        return self.arrival_time - self.departure_time


class Review(models.Model):
    """Passenger review for a completed flight."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, f'{i} Star') for i in range(1, 6)])
    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'flight')
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Review by {self.user.username} for {self.flight.flight_id}"
