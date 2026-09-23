from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable


def reverse(value: str) -> str:
    """Inverte uma string."""
    return value[::-1]


def is_palindrome(value: str, *, ignore_case: bool = True) -> bool:
    """Verifica se uma string é um palíndromo."""
    if ignore_case:
        value = value.casefold()

    return value == value[::-1]


def is_empty(value: str) -> bool:
    """Verifica se a string está vazia."""
    return value == ""


def is_blank(value: str) -> bool:
    """Verifica se a string está vazia ou contém apenas espaços."""
    return value.strip() == ""


def count_words(value: str) -> int:
    """Conta as palavras de uma string."""
    return len(re.findall(r"\S+", value))


def count_characters(
    value: str,
    *,
    ignore_spaces: bool = False,
) -> int:
    """Conta caracteres."""
    if ignore_spaces:
        return sum(not char.isspace() for char in value)

    return len(value)


def first_char(value: str) -> str:
    """Retorna o primeiro caractere."""
    if not value:
        raise ValueError("value cannot be empty.")

    return value[0]


def last_char(value: str) -> str:
    """Retorna o último caractere."""
    if not value:
        raise ValueError("value cannot be empty.")

    return value[-1]


def truncate(
    value: str,
    length: int,
    suffix: str = "...",
) -> str:
    """Limita o tamanho de uma string."""
    if length < 0:
        raise ValueError("length cannot be negative.")

    if len(value) <= length:
        return value

    if len(suffix) >= length:
        return suffix[:length]

    return value[: length - len(suffix)] + suffix


def remove_prefix(value: str, prefix: str) -> str:
    """Remove um prefixo caso ele exista."""
    if value.startswith(prefix):
        return value[len(prefix) :]

    return value


def remove_suffix(value: str, suffix: str) -> str:
    """Remove um sufixo caso ele exista."""
    if value.endswith(suffix):
        return value[: -len(suffix)] if suffix else value

    return value


def repeat(value: str, times: int) -> str:
    """Repete uma string."""
    if times < 0:
        raise ValueError("times cannot be negative.")

    return value * times


def to_snake_case(value: str) -> str:
    """Converte texto para snake_case."""
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value)

    return value.strip("_").lower()


def to_kebab_case(value: str) -> str:
    """Converte texto para kebab-case."""
    return to_snake_case(value).replace("_", "-")


def to_camel_case(value: str) -> str:
    """Converte texto para camelCase."""
    words = re.split(r"[_\-\s]+", value.strip())

    if not words or not words[0]:
        return ""

    return words[0].lower() + "".join(word.capitalize() for word in words[1:] if word)


def to_pascal_case(value: str) -> str:
    """Converte texto para PascalCase."""
    words = re.split(r"[_\-\s]+", value.strip())

    return "".join(word.capitalize() for word in words if word)


def slugify(value: str, separator: str = "-") -> str:
    """Converte texto em um slug adequado para URLs."""
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", separator, value)
    value = re.sub(
        rf"{re.escape(separator)}+",
        separator,
        value,
    )

    return value.strip(separator)


def remove_accents(value: str) -> str:
    """Remove acentos e outros diacríticos."""
    normalized = unicodedata.normalize("NFKD", value)

    return "".join(char for char in normalized if not unicodedata.combining(char))


def only_digits(value: str) -> str:
    """Retorna somente os dígitos presentes na string."""
    return "".join(char for char in value if char.isdigit())


def only_letters(value: str) -> str:
    """Retorna somente as letras presentes na string."""
    return "".join(char for char in value if char.isalpha())


def normalize_spaces(value: str) -> str:
    """Substitui sequências de espaços por um único espaço."""
    return " ".join(value.split())


def lines(value: str) -> list[str]:
    """Converte uma string em uma lista de linhas."""
    return value.splitlines()


def words(value: str) -> list[str]:
    """Converte uma string em uma lista de palavras."""
    return re.findall(r"\S+", value)


def contains_any(value: str, items: Iterable[str]) -> bool:
    """Verifica se a string contém pelo menos um dos itens."""
    return any(item in value for item in items)


def contains_all(value: str, items: Iterable[str]) -> bool:
    """Verifica se a string contém todos os itens."""
    return all(item in value for item in items)


def mask(
    value: str,
    visible_start: int = 0,
    visible_end: int = 0,
    mask_character: str = "*",
) -> str:
    """Oculta parte de uma string."""
    if visible_start < 0 or visible_end < 0:
        raise ValueError("visible_start and visible_end cannot be negative.")

    if len(mask_character) != 1:
        raise ValueError("mask_character must contain exactly one character.")

    if visible_start + visible_end >= len(value):
        return value

    end = len(value) - visible_end

    return value[:visible_start] + mask_character * (end - visible_start) + value[end:]


def common_prefix(a: str, b: str) -> str:
    """Retorna o prefixo comum entre duas strings."""
    size = min(len(a), len(b))
    index = 0

    while index < size and a[index] == b[index]:
        index += 1

    return a[:index]


def common_suffix(a: str, b: str) -> str:
    """Retorna o sufixo comum entre duas strings."""
    size = min(len(a), len(b))
    index = 0

    while index < size and a[-index - 1] == b[-index - 1]:
        index += 1

    return a[len(a) - index :]


def levenshtein_distance(a: str, b: str) -> int:
    """Calcula a distância de Levenshtein entre duas strings."""
    if a == b:
        return 0

    if not a:
        return len(b)

    if not b:
        return len(a)

    previous = list(range(len(b) + 1))

    for i, char_a in enumerate(a, start=1):
        current = [i]

        for j, char_b in enumerate(b, start=1):
            insertion = current[j - 1] + 1
            deletion = previous[j] + 1
            substitution = previous[j - 1] + (char_a != char_b)

            current.append(min(insertion, deletion, substitution))

        previous = current

    return previous[-1]
