class String:
    """Representa uma string com utilitários adicionais."""

    __slots__ = ("value",)

    def __init__(self, value: str = ""):
        self.value = str(value)

    def reverse(self) -> String:
        return String(self.value[::-1])

    def is_empty(self) -> bool:
        return self.value == ""

    def is_blank(self) -> bool:
        return self.value.strip() == ""

    def is_palindrome(self, *, ignore_case: bool = True) -> bool:
        return is_palindrome(
            self.value,
            ignore_case=ignore_case,
        )

    def count_words(self) -> int:
        return count_words(self.value)

    def count_characters(self, *, ignore_spaces: bool = False) -> int:
        return count_characters(
            self.value,
            ignore_spaces=ignore_spaces,
        )

    def first(self) -> str:
        return first_char(self.value)

    def last(self) -> str:
        return last_char(self.value)

    def truncate(
        self,
        length: int,
        suffix: str = "...",
    ) -> String:
        return String(
            truncate(
                self.value,
                length,
                suffix,
            )
        )

    def remove_prefix(self, prefix: str) -> String:
        return String(
            remove_prefix(
                self.value,
                prefix,
            )
        )

    def remove_suffix(self, suffix: str) -> String:
        return String(
            remove_suffix(
                self.value,
                suffix,
            )
        )

    def repeat(self, times: int) -> String:
        return String(
            repeat(
                self.value,
                times,
            )
        )

    def snake_case(self) -> String:
        return String(to_snake_case(self.value))

    def kebab_case(self) -> String:
        return String(to_kebab_case(self.value))

    def camel_case(self) -> String:
        return String(to_camel_case(self.value))

    def pascal_case(self) -> String:
        return String(to_pascal_case(self.value))

    def slugify(self, separator: str = "-") -> String:
        return String(
            slugify(
                self.value,
                separator,
            )
        )

    def remove_accents(self) -> String:
        return String(remove_accents(self.value))

    def only_digits(self) -> String:
        return String(only_digits(self.value))

    def only_letters(self) -> String:
        return String(only_letters(self.value))

    def normalize_spaces(self) -> String:
        return String(normalize_spaces(self.value))

    def lines(self) -> list[str]:
        return lines(self.value)

    def words(self) -> list[str]:
        return words(self.value)

    def contains_any(self, items: Iterable[str]) -> bool:
        return contains_any(self.value, items)

    def contains_all(self, items: Iterable[str]) -> bool:
        return contains_all(self.value, items)

    def mask(
        self,
        visible_start: int = 0,
        visible_end: int = 0,
        mask_character: str = "*",
    ) -> String:
        return String(
            mask(
                self.value,
                visible_start,
                visible_end,
                mask_character,
            )
        )

    def common_prefix(self, other: str | String) -> String:
        other_value = other.value if isinstance(other, String) else str(other)

        return String(
            common_prefix(
                self.value,
                other_value,
            )
        )

    def common_suffix(self, other: str | String) -> String:
        other_value = other.value if isinstance(other, String) else str(other)

        return String(
            common_suffix(
                self.value,
                other_value,
            )
        )

    def levenshtein_distance(self, other: str | String) -> int:
        other_value = other.value if isinstance(other, String) else str(other)

        return levenshtein_distance(
            self.value,
            other_value,
        )

    def upper(self) -> String:
        return String(self.value.upper())

    def lower(self) -> String:
        return String(self.value.lower())

    def title(self) -> String:
        return String(self.value.title())

    def strip(self, chars: str | None = None) -> String:
        return String(self.value.strip(chars))

    def replace(
        self,
        old: str,
        new: str,
        count: int = -1,
    ) -> String:
        return String(
            self.value.replace(
                old,
                new,
                count,
            )
        )

    def starts_with(self, prefix: str) -> bool:
        return self.value.startswith(prefix)

    def ends_with(self, suffix: str) -> bool:
        return self.value.endswith(suffix)

    def contains(self, value: str) -> bool:
        return value in self.value

    def to_str(self) -> str:
        return self.value

    def copy(self) -> String:
        return String(self.value)

    def __len__(self) -> int:
        return len(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __contains__(self, item: str) -> bool:
        return item in self.value

    def __add__(self, other: str | String) -> String:
        other_value = other.value if isinstance(other, String) else str(other)

        return String(self.value + other_value)

    def __radd__(self, other: str | String) -> String:
        other_value = other.value if isinstance(other, String) else str(other)

        return String(other_value + self.value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, String):
            return self.value == other.value

        if isinstance(other, str):
            return self.value == other

        return NotImplemented

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"String({self.value!r})"
