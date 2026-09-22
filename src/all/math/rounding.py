from math import ceil, floor


def round_down(value: float) -> int:
    return floor(value)


def round_up(value: float) -> int:
    return ceil(value)


def truncate(value: float) -> int:
    return int(value)


def round_to(value: float, digits: int = 0) -> float:
    return round(value, digits)
