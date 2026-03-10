"""
bookings/repositories.py — BookingRepository: all ORM queries for bookings.
"""
import logging
from django.core.paginator import Paginator

from .models import Booking

logger = logging.getLogger('apps.bookings')


class BookingRepository:

    @staticmethod
    def create(booking_data: dict) -> Booking:
        return Booking.objects.create(**booking_data)

    @staticmethod
    def get_for_user(user, page: int = 1, per_page: int = 20):
        """Return paginated bookings for a user, with flight pre-fetched."""
        qs = Booking.objects.filter(user=user).select_related('flight')
        paginator = Paginator(qs, per_page)
        return paginator.get_page(page)

    @staticmethod
    def get_by_id_for_user(booking_id: int, user) -> Booking:
        return Booking.objects.select_related('flight').get(id=booking_id, user=user)

    @staticmethod
    def seat_is_taken(flight, seat_number: str) -> bool:
        return Booking.objects.filter(
            flight=flight,
            seat_number=seat_number,
        ).exclude(status='cancelled').exists()

    @staticmethod
    def cancel(booking: Booking) -> Booking:
        booking.status = 'cancelled'
        booking.save(update_fields=['status', 'updated_at'])
        return booking
