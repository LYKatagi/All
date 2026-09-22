"""Base Date class for the all library."""

from __future__ import annotations

from datetime import date as _date
from datetime import datetime as _datetime
from datetime import timedelta


class Date:
    """Represents a calendar date."""

    def __init__(self, year: int, month: int, day: int) -> None:
        self._date = _date(year, month, day)

    @classmethod
    def today(cls) -> Date:
        """Return today's date."""
        current = _date.today()
        return cls(current.year, current.month, current.day)

    @classmethod
    def from_string(
        cls,
        value: str,
        format: str = "%Y-%m-%d",
    ) -> Date:
        """Create a Date from a formatted string."""
        parsed = _datetime.strptime(value, format).date()
        return cls(parsed.year, parsed.month, parsed.day)

    @classmethod
    def from_date(cls, value: _date) -> Date:
        """Create a Date from a datetime.date object."""
        return cls(value.year, value.month, value.day)

    @property
    def year(self) -> int:
        return self._date.year

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def day(self) -> int:
        return self._date.day

    @property
    def weekday(self) -> int:
        """Return the weekday.

        Monday is 0 and Sunday is 6.
        """
        return self._date.weekday()

    def add_days(self, days: int) -> Date:
        """Return a new Date with days added."""
        result = self._date + timedelta(days=days)
        return Date.from_date(result)

    def subtract_days(self, days: int) -> Date:
        """Return a new Date with days subtracted."""
        return self.add_days(-days)

    def days_until(self, other: Date) -> int:
        """Return the number of days until another date."""
        if not isinstance(other, Date):
            raise TypeError("other must be a Date.")

        return (other._date - self._date).days

    def format(self, format: str = "%Y-%m-%d") -> str:
        """Format the date as a string."""
        return self._date.strftime(format)

    def to_date(self) -> _date:
        """Return the underlying datetime.date."""
        return self._date

    def __str__(self) -> str:
        return self.format()

    def __repr__(self) -> str:
        return f"Date({self.year}, {self.month}, {self.day})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Date):
            return self._date == other._date

        return NotImplemented

    def __lt__(self, other: Date) -> bool:
        if isinstance(other, Date):
            return self._date < other._date

        return NotImplemented

    def __le__(self, other: Date) -> bool:
        if isinstance(other, Date):
            return self._date <= other._date

        return NotImplemented

    def __gt__(self, other: Date) -> bool:
        if isinstance(other, Date):
            return self._date > other._date

        return NotImplemented

    def __ge__(self, other: Date) -> bool:
        if isinstance(other, Date):
            return self._date >= other._date

        return NotImplemented
