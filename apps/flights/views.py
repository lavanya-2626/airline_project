"""
flights/views.py — Thin HTTP handlers for home and flight search.
"""
import logging
from django.shortcuts import render

from .services import FlightService

logger = logging.getLogger('apps.flights')


def home(request):
    """Home page: show featured active flights."""
    flights = FlightService.get_featured_flights(limit=6)
    return render(request, 'flights/home.html', {'flights': flights})


def search_flights(request):
    """Search flights by source, destination and date with pagination."""
    source = request.GET.get('source', '').strip()
    destination = request.GET.get('destination', '').strip()
    travel_date = request.GET.get('travel_date', '').strip() or None
    page = request.GET.get('page', 1)

    flights_page = FlightService.search_flights(
        source=source,
        destination=destination,
        travel_date=travel_date,
        page=page,
    )

    return render(request, 'flights/search_flight.html', {
        'flights': flights_page,
        'source': source,
        'destination': destination,
        'travel_date': travel_date or '',
    })
