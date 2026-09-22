from __future__ import annotations


def clamp(value: float, minimum: float, maximum: float) -> float:
    if minimum > maximum:
        raise ValueError("minimum cannot be greater than maximum.")

    return max(minimum, min(value, maximum))


def lerp(start: float, end: float, amount: float) -> float:
    return start + (end - start) * amount


def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)
