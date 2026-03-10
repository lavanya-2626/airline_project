"""
flights/services.py — FlightService: business logic for flight operations.
"""
import logging
from apps.core.exceptions import FlightNotFoundError
from .repositories import FlightRepository

logger = logging.getLogger('apps.flights')


class FlightService:

    @staticmethod
    def get_featured_flights(limit: int = 6):
        return FlightRepository.get_featured(limit)

    @staticmethod
    def search_flights(source='', destination='', travel_date=None, page=1):
        return FlightRepository.search(
            source=source,
            destination=destination,
            travel_date=travel_date,
            page=page,
        )

    @staticmethod
    def get_flight(flight_id: str):
        try:
            return FlightRepository.get_by_id(flight_id)
        except Exception:
            raise FlightNotFoundError(f"Flight #{flight_id} not found.")
