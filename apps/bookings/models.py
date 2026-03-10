"""
bookings/models.py — Booking domain model.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse

from apps.flights.models import Flight


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
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
    )
    # Passenger travel document details
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
        return f"{self.booking_id} — {self.passenger_name}"

    def get_absolute_url(self):
        return reverse('booking_confirmation', args=[self.id])

    def can_cancel(self):
        return self.status in ['pending', 'confirmed']

    def get_duration(self):
        return self.flight.arrival_time - self.flight.departure_time
