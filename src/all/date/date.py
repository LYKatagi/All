"""Date utility functions."""

from .base_class import Date


def today() -> Date:
    """Return today's date."""
    return Date.today()


def from_string(
    value: str,
    format: str = "%Y-%m-%d",
) -> Date:
    """Create a Date from a formatted string."""
    return Date.from_string(value, format)
