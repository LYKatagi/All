from __future__ import annotations

from math import sqrt


def quadratic_roots(a: float, b: float, c: float) -> tuple[complex, complex]:
    """Calcula as duas raízes de uma equação quadrática."""
    if a == 0:
        raise ValueError("a cannot be zero.")

    delta = b**2 - 4 * a * c
    root = sqrt(delta) if delta >= 0 else complex(delta) ** 0.5

    return (
        (-b + root) / (2 * a),
        (-b - root) / (2 * a),
    )


def discriminant(a: float, b: float, c: float) -> float:
    """Calcula o discriminante de uma equação quadrática."""
    if a == 0:
        raise ValueError("a cannot be zero.")

    return b**2 - 4 * a * c


def power(base: float, exponent: float) -> float:
    """Calcula uma potência."""
    return base**exponent


def square(value: float) -> float:
    """Calcula o quadrado de um número."""
    return value**2


def cube(value: float) -> float:
    """Calcula o cubo de um número."""
    return value**3


def absolute(value: float) -> float:
    """Retorna o valor absoluto."""
    return abs(value)


def sign(value: float) -> int:
    """Retorna -1, 0 ou 1 conforme o sinal do número."""
    if value > 0:
        return 1

    if value < 0:
        return -1

    return 0


def average(a: float, b: float) -> float:
    """Calcula a média de dois valores."""
    return (a + b) / 2


def midpoint(a: float, b: float) -> float:
    """Retorna o ponto médio entre dois valores."""
    return (a + b) / 2
