from __future__ import annotations

from math import pi, sqrt


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calcula a distância entre dois pontos."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def distance_squared(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calcula a distância ao quadrado entre dois pontos."""
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def midpoint(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> tuple[float, float]:
    """Retorna o ponto médio entre dois pontos."""
    return (
        (x1 + x2) / 2,
        (y1 + y2) / 2,
    )


def hypotenuse(a: float, b: float) -> float:
    """Calcula a hipotenusa de um triângulo retângulo."""
    return sqrt(a**2 + b**2)


def triangle_area(
    base: float,
    height: float,
) -> float:
    """Calcula a área de um triângulo."""
    if base < 0 or height < 0:
        raise ValueError("base and height cannot be negative.")

    return (base * height) / 2


def rectangle_area(
    width: float,
    height: float,
) -> float:
    """Calcula a área de um retângulo."""
    if width < 0 or height < 0:
        raise ValueError("width and height cannot be negative.")

    return width * height


def rectangle_perimeter(
    width: float,
    height: float,
) -> float:
    """Calcula o perímetro de um retângulo."""
    if width < 0 or height < 0:
        raise ValueError("width and height cannot be negative.")

    return 2 * (width + height)


def square_area(side: float) -> float:
    """Calcula a área de um quadrado."""
    if side < 0:
        raise ValueError("side cannot be negative.")

    return side**2


def square_perimeter(side: float) -> float:
    """Calcula o perímetro de um quadrado."""
    if side < 0:
        raise ValueError("side cannot be negative.")

    return side * 4


def circle_area(radius: float) -> float:
    """Calcula a área de um círculo."""
    if radius < 0:
        raise ValueError("radius cannot be negative.")

    return pi * radius**2


def circle_circumference(radius: float) -> float:
    """Calcula a circunferência de um círculo."""
    if radius < 0:
        raise ValueError("radius cannot be negative.")

    return 2 * pi * radius


def sphere_volume(radius: float) -> float:
    """Calcula o volume de uma esfera."""
    if radius < 0:
        raise ValueError("radius cannot be negative.")

    return (4 / 3) * pi * radius**3


def sphere_surface_area(radius: float) -> float:
    """Calcula a área superficial de uma esfera."""
    if radius < 0:
        raise ValueError("radius cannot be negative.")

    return 4 * pi * radius**2


def triangle_perimeter(
    a: float,
    b: float,
    c: float,
) -> float:
    """Calcula o perímetro de um triângulo."""
    if min(a, b, c) < 0:
        raise ValueError("side lengths cannot be negative.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("the given sides cannot form a triangle.")

    return a + b + c


def triangle_area_from_sides(
    a: float,
    b: float,
    c: float,
) -> float:
    """Calcula a área de um triângulo usando a fórmula de Heron."""
    perimeter = triangle_perimeter(a, b, c)
    semiperimeter = perimeter / 2

    return sqrt(
        semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)
    )


def is_point_inside_circle(
    x: float,
    y: float,
    center_x: float,
    center_y: float,
    radius: float,
) -> bool:
    """Verifica se um ponto está dentro ou sobre um círculo."""
    if radius < 0:
        raise ValueError("radius cannot be negative.")

    return distance_squared(x, y, center_x, center_y) <= radius**2


def is_point_inside_rectangle(
    x: float,
    y: float,
    left: float,
    top: float,
    width: float,
    height: float,
) -> bool:
    """Verifica se um ponto está dentro ou sobre um retângulo."""
    if width < 0 or height < 0:
        raise ValueError("width and height cannot be negative.")

    return left <= x <= left + width and top <= y <= top + height
