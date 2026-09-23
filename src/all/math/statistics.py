from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from math import sqrt

Number = int | float


def _values(data: Iterable[Number]) -> list[float]:
    values = [float(value) for value in data]

    if not values:
        raise ValueError("data cannot be empty.")

    return values


def mean(data: Iterable[Number]) -> float:
    """Calcula a média aritmética."""
    values = _values(data)
    return sum(values) / len(values)


def weighted_mean(
    data: Iterable[Number],
    weights: Iterable[Number],
) -> float:
    """Calcula a média ponderada."""
    values = list(data)
    weight_values = list(weights)

    if not values:
        raise ValueError("data cannot be empty.")

    if len(values) != len(weight_values):
        raise ValueError("data and weights must have the same length.")

    total_weight = sum(weight_values)

    if total_weight == 0:
        raise ZeroDivisionError("the sum of weights cannot be zero.")

    return (
        sum(value * weight for value, weight in zip(values, weight_values))
        / total_weight
    )


def median(data: Iterable[Number]) -> float:
    """Calcula a mediana."""
    values = sorted(_values(data))
    size = len(values)

    middle = size // 2

    if size % 2 == 0:
        return (values[middle - 1] + values[middle]) / 2

    return values[middle]


def modes(data: Iterable[Number]) -> list[float]:
    """Retorna todos os valores que possuem a maior frequência."""
    values = _values(data)
    counts = Counter(values)
    highest = max(counts.values())

    return [value for value in dict.fromkeys(values) if counts[value] == highest]


def mode(data: Iterable[Number]) -> float:
    """Retorna a primeira moda encontrada."""
    return modes(data)[0]


def minimum(data: Iterable[Number]) -> float:
    """Retorna o menor valor."""
    return min(_values(data))


def maximum(data: Iterable[Number]) -> float:
    """Retorna o maior valor."""
    return max(_values(data))


def data_range(data: Iterable[Number]) -> float:
    """Retorna a amplitude dos dados."""
    values = _values(data)
    return max(values) - min(values)


def variance(
    data: Iterable[Number],
    sample: bool = True,
) -> float:
    """
    Calcula a variância.

    Quando sample=True, calcula a variância amostral.
    Quando sample=False, calcula a variância populacional.
    """
    values = _values(data)

    if sample and len(values) < 2:
        raise ValueError("at least two values are required for sample variance.")

    center = mean(values)
    squared_differences = sum((value - center) ** 2 for value in values)

    denominator = len(values) - 1 if sample else len(values)

    return squared_differences / denominator


def standard_deviation(
    data: Iterable[Number],
    sample: bool = True,
) -> float:
    """Calcula o desvio padrão."""
    return sqrt(variance(data, sample=sample))


def population_variance(data: Iterable[Number]) -> float:
    """Calcula a variância populacional."""
    return variance(data, sample=False)


def population_standard_deviation(data: Iterable[Number]) -> float:
    """Calcula o desvio padrão populacional."""
    return standard_deviation(data, sample=False)


def percentile(
    data: Iterable[Number],
    percent: float,
) -> float:
    """
    Calcula um percentil usando interpolação linear.

    percent deve estar entre 0 e 100.
    """
    values = sorted(_values(data))

    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100.")

    if len(values) == 1:
        return values[0]

    position = (len(values) - 1) * (percent / 100)
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)

    fraction = position - lower

    return values[lower] + (values[upper] - values[lower]) * fraction


def quartiles(data: Iterable[Number]) -> tuple[float, float, float]:
    """Retorna Q1, Q2 e Q3."""
    values = _values(data)

    return (
        percentile(values, 25),
        percentile(values, 50),
        percentile(values, 75),
    )


def interquartile_range(data: Iterable[Number]) -> float:
    """Retorna o intervalo interquartil (Q3 - Q1)."""
    q1, _, q3 = quartiles(data)
    return q3 - q1


def covariance(
    x: Iterable[Number],
    y: Iterable[Number],
    sample: bool = True,
) -> float:
    """Calcula a covariância entre dois conjuntos."""
    x_values = _values(x)
    y_values = _values(y)

    if len(x_values) != len(y_values):
        raise ValueError("x and y must have the same length.")

    if sample and len(x_values) < 2:
        raise ValueError("at least two values are required for sample covariance.")

    x_mean = mean(x_values)
    y_mean = mean(y_values)

    total = sum(
        (x_value - x_mean) * (y_value - y_mean)
        for x_value, y_value in zip(x_values, y_values)
    )

    denominator = len(x_values) - 1 if sample else len(x_values)

    return total / denominator


def correlation(
    x: Iterable[Number],
    y: Iterable[Number],
) -> float:
    """Calcula o coeficiente de correlação de Pearson."""
    x_values = _values(x)
    y_values = _values(y)

    if len(x_values) != len(y_values):
        raise ValueError("x and y must have the same length.")

    x_mean = mean(x_values)
    y_mean = mean(y_values)

    numerator = sum(
        (x_value - x_mean) * (y_value - y_mean)
        for x_value, y_value in zip(x_values, y_values)
    )

    x_variation = sum((value - x_mean) ** 2 for value in x_values)
    y_variation = sum((value - y_mean) ** 2 for value in y_values)

    denominator = sqrt(x_variation * y_variation)

    if denominator == 0:
        raise ZeroDivisionError(
            "correlation is undefined when one dataset has no variation."
        )

    return numerator / denominator


def geometric_mean(data: Iterable[Number]) -> float:
    """Calcula a média geométrica."""
    values = _values(data)

    if any(value <= 0 for value in values):
        raise ValueError("geometric mean requires all values to be positive.")

    product = 1.0

    for value in values:
        product *= value

    return product ** (1 / len(values))


def harmonic_mean(data: Iterable[Number]) -> float:
    """Calcula a média harmônica."""
    values = _values(data)

    if any(value <= 0 for value in values):
        raise ValueError("harmonic mean requires all values to be positive.")

    return len(values) / sum(1 / value for value in values)


def root_mean_square(data: Iterable[Number]) -> float:
    """Calcula a raiz quadrática média (RMS)."""
    values = _values(data)

    return sqrt(sum(value**2 for value in values) / len(values))


def z_score(
    value: Number,
    data: Iterable[Number],
    sample: bool = True,
) -> float:
    """Calcula o z-score de um valor em relação a um conjunto."""
    values = _values(data)
    deviation = standard_deviation(values, sample=sample)

    if deviation == 0:
        raise ZeroDivisionError(
            "z-score is undefined when the standard deviation is zero."
        )

    return (value - mean(values)) / deviation
