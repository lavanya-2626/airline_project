"""
bookings/views.py — Thin HTTP handlers for booking operations.
"""
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.flights.services import FlightService
from apps.core.exceptions import (
    FlightNotAvailableError,
    FlightNotFoundError,
    SeatAlreadyTakenError,
    BookingError,
)
from .forms import BookingForm
from .services import BookingService

logger = logging.getLogger('apps.bookings')


@login_required(login_url='login')
def book_flight(request, flight_id):
    """Display booking form and process a new booking."""
    try:
        flight = FlightService.get_flight(flight_id)
    except FlightNotFoundError:
        messages.error(request, 'Flight not found.')
        return redirect('search_flights')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = BookingService.create_booking(
                    user=request.user,
                    flight=flight,
                    passenger_data=form.cleaned_data,
                )
                messages.success(
                    request,
                    f'Booking confirmed! Your reference: {booking.booking_id}'
                )
                return redirect('booking_confirmation', booking_id=booking.id)
            except SeatAlreadyTakenError as e:
                messages.error(request, str(e))
            except FlightNotAvailableError as e:
                messages.error(request, str(e))
            except BookingError as e:
                messages.error(request, str(e))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = BookingForm()

    return render(request, 'bookings/booking.html', {'flight': flight, 'form': form})


@login_required(login_url='login')
def booking_confirmation(request, booking_id):
    """Show booking confirmation details."""
    try:
        booking = BookingService.get_booking_for_user(booking_id, request.user)
    except BookingError:
        messages.error(request, 'Booking not found.')
        return redirect('booking_history')

    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})


@login_required(login_url='login')
def booking_history(request):
    """List all bookings for the logged-in user (paginated)."""
    page = request.GET.get('page', 1)
    bookings = BookingService.get_user_bookings(request.user, page=page)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})


@login_required(login_url='login')
def cancel_booking(request, booking_id):
    """Cancel a booking and restore the seat."""
    try:
        booking = BookingService.get_booking_for_user(booking_id, request.user)
        BookingService.cancel_booking(booking)
        messages.success(request, f'Booking {booking.booking_id} has been cancelled.')
    except BookingError as e:
        messages.error(request, str(e))
    return redirect('booking_history')
