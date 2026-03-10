"""
core/exceptions.py — Custom domain exceptions for structured error handling.
"""


class AirlineBaseError(Exception):
    """Base exception for all airline project errors."""
    pass


class FlightNotAvailableError(AirlineBaseError):
    """Raised when a flight has no available seats."""
    pass


class FlightNotFoundError(AirlineBaseError):
    """Raised when a requested flight does not exist."""
    pass


class BookingError(AirlineBaseError):
    """Raised when a booking operation fails."""
    pass


class SeatAlreadyTakenError(BookingError):
    """Raised when the requested seat is already booked."""
    pass


class AuthError(AirlineBaseError):
    """Raised for authentication and authorisation failures."""
    pass


class UserAlreadyExistsError(AuthError):
    """Raised when username or email is already registered."""
    pass
