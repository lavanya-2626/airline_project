"""
bookings/services.py — BookingService: all booking business logic.

KEY FIX: The old code did `flight.seats_available -= 1; flight.save()`
which is a race condition — two concurrent requests can both read the
same count and both decrement it, leading to overbooking.

The fix uses Django's F() expression + filter(seats_available__gt=0)
so the decrement is done atomically in the database in a single UPDATE.
"""
import logging
from django.db import transaction
from django.db.models import F

from apps.core.exceptions import (
    FlightNotAvailableError,
    SeatAlreadyTakenError,
    BookingError,
)
from apps.core.utils import generate_booking_id
from apps.flights.models import Flight
from .models import Booking
from .repositories import BookingRepository

logger = logging.getLogger('apps.bookings')


class BookingService:

    @staticmethod
    @transaction.atomic
    def create_booking(user, flight: Flight, passenger_data: dict) -> Booking:
        """
        Atomically reserve a seat and create a Booking record.

        Steps:
          1. Check seat is not already taken.
          2. Atomically decrement seats_available (race-condition-safe).
          3. Create the Booking record.

        Raises:
          FlightNotAvailableError  — no seats left
          SeatAlreadyTakenError    — seat already booked
          BookingError             — any other failure
        """
        seat_number = passenger_data['seat_number']

        # 1. Check seat conflict
        if BookingRepository.seat_is_taken(flight, seat_number):
            raise SeatAlreadyTakenError(
                f"Seat {seat_number} is already taken. Please choose another."
            )

        # 2. Atomic seat decrement — only updates if seats_available > 0
        updated = Flight.objects.filter(
            pk=flight.pk,
            seats_available__gt=0,
        ).update(seats_available=F('seats_available') - 1)

        if updated == 0:
            raise FlightNotAvailableError(
                "Sorry, this flight is fully booked. No seats available."
            )

        # 3. Create booking record
        booking = BookingRepository.create({
            'booking_id': generate_booking_id(),
            'user': user,
            'flight': flight,
            'passenger_name': passenger_data['passenger_name'],
            'passenger_email': passenger_data['passenger_email'],
            'passenger_phone': passenger_data['passenger_phone'],
            'seat_number': seat_number,
            'status': 'confirmed',
            'total_price': flight.price,
        })

        logger.info(
            "Booking created: %s | user=%s | flight=%s | seat=%s",
            booking.booking_id, user.username, flight.flight_id, seat_number,
        )
        return booking

    @staticmethod
    def get_user_bookings(user, page: int = 1):
        return BookingRepository.get_for_user(user, page=page)

    @staticmethod
    def get_booking_for_user(booking_id: int, user) -> Booking:
        try:
            return BookingRepository.get_by_id_for_user(booking_id, user)
        except Booking.DoesNotExist:
            raise BookingError("Booking not found.")

    @staticmethod
    @transaction.atomic
    def cancel_booking(booking: Booking) -> Booking:
        if not booking.can_cancel():
            raise BookingError(
                f"Booking {booking.booking_id} cannot be cancelled (status: {booking.status})."
            )
        # Return the seat
        Flight.objects.filter(pk=booking.flight.pk).update(
            seats_available=F('seats_available') + 1
        )
        updated = BookingRepository.cancel(booking)
        logger.info("Booking cancelled: %s", booking.booking_id)
        return updated
