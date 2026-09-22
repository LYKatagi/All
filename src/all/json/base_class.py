"""Core JSON class implementation."""

from __future__ import annotations

import json as _json
from pathlib import Path
from typing import Any


class JSON:
    """Represents a JSON document."""

    def __init__(self, data: dict[str, Any] | None = None) -> None:
        self._data: dict[str, Any] = data.copy() if data else {}

    @classmethod
    def load(
        cls,
        path: str | Path,
        *,
        encoding: str = "utf-8",
    ) -> JSON:
        """Load a JSON document from a file."""
        with Path(path).open("r", encoding=encoding) as file:
            data = _json.load(file)

        if not isinstance(data, dict):
            raise TypeError("JSON root must be an object.")

        return cls(data)

    def save(
        self,
        path: str | Path,
        *,
        encoding: str = "utf-8",
        indent: int | None = 4,
    ) -> None:
        """Save the JSON document to a file."""
        with Path(path).open("w", encoding=encoding) as file:
            _json.dump(
                self._data,
                file,
                indent=indent,
                ensure_ascii=False,
            )

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the document."""
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> JSON:
        """Set a value and return this JSON object."""
        self._data[key] = value
        return self

    def remove(self, key: str) -> Any:
        """Remove and return a value."""
        return self._data.pop(key)

    def has(self, key: str) -> bool:
        """Check whether a key exists."""
        return key in self._data

    def clear(self) -> None:
        """Remove all data."""
        self._data.clear()

    def to_dict(self) -> dict[str, Any]:
        """Return the document as a dictionary."""
        return self._data.copy()

    def dumps(
        self,
        *,
        indent: int | None = None,
        ensure_ascii: bool = False,
    ) -> str:
        """Serialize the document to a JSON string."""
        return _json.dumps(
            self._data,
            indent=indent,
            ensure_ascii=ensure_ascii,
        )

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._data[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self._data

    def __repr__(self) -> str:
        return f"JSON({self._data!r})"

    def __str__(self) -> str:
        return self.dumps(indent=4, ensure_ascii=False)
