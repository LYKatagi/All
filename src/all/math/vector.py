from __future__ import annotations

from collections.abc import Iterator
from math import sqrt


class Vector:
    """Representa um vetor bidimensional."""

    __slots__ = ("x", "y")

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    @property
    def magnitude(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    @property
    def magnitude_squared(self) -> float:
        return self.x**2 + self.y**2

    def normalized(self) -> Vector:
        magnitude = self.magnitude

        if magnitude == 0:
            return Vector()

        return Vector(
            self.x / magnitude,
            self.y / magnitude,
        )

    def dot(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def distance_to(self, other: Vector) -> float:
        return (self - other).magnitude

    def distance_squared_to(self, other: Vector) -> float:
        return (self - other).magnitude_squared

    def copy(self) -> Vector:
        return Vector(self.x, self.y)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, value: float) -> Vector:
        return Vector(
            self.x * value,
            self.y * value,
        )

    def __rmul__(self, value: float) -> Vector:
        return self * value

    def __truediv__(self, value: float) -> Vector:
        if value == 0:
            raise ZeroDivisionError("Cannot divide a vector by zero.")

        return Vector(
            self.x / value,
            self.y / value,
        )

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y)

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
