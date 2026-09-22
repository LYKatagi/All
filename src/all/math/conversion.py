from .constants import DEG_TO_RAD, RAD_TO_DEG


def degrees_to_radians(degrees: float) -> float:
    return degrees * DEG_TO_RAD


def radians_to_degrees(radians: float) -> float:
    return radians * RAD_TO_DEG


def percentage(value: float, total: float) -> float:
    if total == 0:
        raise ZeroDivisionError("total cannot be zero.")

    return (value / total) * 100


def percent_of(value: float, percentage: float) -> float:
    return value * (percentage / 100)
