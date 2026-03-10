"""
flights/repositories.py — FlightRepository: all ORM queries for flights.
Services call this; views never touch the ORM directly.
"""
import logging
from typing import Optional
from django.core.paginator import Paginator

from .models import Flight

logger = logging.getLogger('apps.flights')


class FlightRepository:

    @staticmethod
    def get_featured(limit: int = 6):
        """Return a small selection of active flights for the home page."""
        return Flight.objects.filter(is_active=True).order_by('departure_time')[:limit]

    @staticmethod
    def search(
        source: str = '',
        destination: str = '',
        travel_date: Optional[str] = None,
        page: int = 1,
        per_page: int = 10,
    ):
        """
        Search active flights by source, destination and/or date.
        Returns a Django Page object (paginated).
        """
        qs = Flight.objects.filter(is_active=True)

        if source:
            qs = qs.filter(source__icontains=source)
        if destination:
            qs = qs.filter(destination__icontains=destination)
        if travel_date:
            qs = qs.filter(departure_time__date=travel_date)

        paginator = Paginator(qs, per_page)
        return paginator.get_page(page)

    @staticmethod
    def get_by_id(flight_id: str) -> Flight:
        """Fetch a single flight by primary key or raise Flight.DoesNotExist."""
        return Flight.objects.get(pk=flight_id)
