"""
core/utils.py — Shared utility helpers used across all apps.
"""
import uuid
import logging

logger = logging.getLogger(__name__)


def generate_booking_id() -> str:
    """Generate a unique booking reference like BK-A1B2C3D4."""
    return f"BK-{uuid.uuid4().hex[:8].upper()}"


def generate_flight_id(airline_code: str = "FL") -> str:
    """Generate a unique flight ID like FL-1A2B3C."""
    return f"{airline_code.upper()}-{uuid.uuid4().hex[:6].upper()}"


def truncate_string(value: str, max_length: int = 100) -> str:
    """Truncate a string to max_length with ellipsis."""
    if len(value) <= max_length:
        return value
    return value[:max_length - 3] + "..."
