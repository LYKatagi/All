from pathlib import Path


def read_file(file_path: str | Path, *, encoding: str = "utf-8") -> str:
    """Read the contents of a file and return it as a string."""
    with Path(file_path).open("r", encoding=encoding) as file:
        return file.read()


def dump_file(file_path: str | Path, data: str, *, encoding: str = "utf-8") -> None:
    """Write a string to a file."""
    with Path(file_path).open("w", encoding=encoding) as file:
        file.write(data)
