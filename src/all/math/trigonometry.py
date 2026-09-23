from __future__ import annotations

from math import (
    acos as _acos,
)
from math import (
    asin as _asin,
)
from math import (
    atan as _atan,
)
from math import (
    atan2 as _atan2,
)
from math import (
    cos as _cos,
)
from math import (
    degrees as _degrees,
)
from math import (
    radians as _radians,
)
from math import (
    sin as _sin,
)
from math import (
    tan as _tan,
)


def sin(angle: float) -> float:
    """Calcula o seno de um ângulo em radianos."""
    return _sin(angle)


def cos(angle: float) -> float:
    """Calcula o cosseno de um ângulo em radianos."""
    return _cos(angle)


def tan(angle: float) -> float:
    """Calcula a tangente de um ângulo em radianos."""
    return _tan(angle)


def asin(value: float) -> float:
    """Calcula o arco-seno."""
    return _asin(value)


def acos(value: float) -> float:
    """Calcula o arco-cosseno."""
    return _acos(value)


def atan(value: float) -> float:
    """Calcula o arco-tangente."""
    return _atan(value)


def atan2(y: float, x: float) -> float:
    """Calcula o arco-tangente usando os componentes Y e X."""
    return _atan2(y, x)


def degrees(radians: float) -> float:
    """Converte radianos para graus."""
    return _degrees(radians)


def radians(degrees_value: float) -> float:
    """Converte graus para radianos."""
    return _radians(degrees_value)


def sec(angle: float) -> float:
    """Calcula a secante."""
    value = _cos(angle)

    if value == 0:
        raise ZeroDivisionError("secant is undefined for this angle.")

    return 1 / value


def csc(angle: float) -> float:
    """Calcula a cossecante."""
    value = _sin(angle)

    if value == 0:
        raise ZeroDivisionError("cosecant is undefined for this angle.")

    return 1 / value


def cot(angle: float) -> float:
    """Calcula a cotangente."""
    value = _tan(angle)

    if value == 0:
        raise ZeroDivisionError("cotangent is undefined for this angle.")

    return 1 / value


def sin_degrees(angle: float) -> float:
    """Calcula o seno de um ângulo em graus."""
    return _sin(_radians(angle))


def cos_degrees(angle: float) -> float:
    """Calcula o cosseno de um ângulo em graus."""
    return _cos(_radians(angle))


def tan_degrees(angle: float) -> float:
    """Calcula a tangente de um ângulo em graus."""
    return _tan(_radians(angle))


def vector_angle(x: float, y: float) -> float:
    """Retorna o ângulo de um vetor em radianos."""
    return _atan2(y, x)


def vector_angle_degrees(x: float, y: float) -> float:
    """Retorna o ângulo de um vetor em graus."""
    return _degrees(_atan2(y, x))


def opposite_from_angle(
    hypotenuse: float,
    angle: float,
) -> float:
    """Calcula o cateto oposto usando ângulo em radianos."""
    return hypotenuse * _sin(angle)


def adjacent_from_angle(
    hypotenuse: float,
    angle: float,
) -> float:
    """Calcula o cateto adjacente usando ângulo em radianos."""
    return hypotenuse * _cos(angle)


def hypotenuse_from_angle(
    opposite: float,
    angle: float,
) -> float:
    """Calcula a hipotenusa usando o cateto oposto."""
    sine = _sin(angle)

    if sine == 0:
        raise ZeroDivisionError("cannot calculate hypotenuse for this angle.")

    return opposite / sine
