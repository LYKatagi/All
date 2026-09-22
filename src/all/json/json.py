"""JSON utilities for the all library."""

import json as _json
from pathlib import Path
from typing import Any

from all.utils.file import dump_file, read_file


def load(path: str | Path, *, encoding: str = "utf-8") -> Any:
    """Load JSON data from a file."""
    return _json.loads(read_file(path, encoding=encoding))


def dump(
    path: str | Path,
    data: Any,
    *,
    encoding: str = "utf-8",
    indent: int | None = 4,
) -> None:
    """Write JSON data to a file."""
    dump_file(
        path, _json.dumps(data, indent=indent, ensure_ascii=False), encoding=encoding
    )


def loads(data: str | bytes | bytearray) -> Any:
    """Parse JSON data from a string or bytes-like object."""
    return _json.loads(data)


def dumps(
    data: Any,
    *,
    indent: int | None = None,
    ensure_ascii: bool = True,
) -> str:
    """Serialize Python data into a JSON string."""
    return _json.dumps(
        data,
        indent=indent,
        ensure_ascii=ensure_ascii,
    )
