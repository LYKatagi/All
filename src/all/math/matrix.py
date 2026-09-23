from __future__ import annotations

from collections.abc import Iterable, Iterator, Sequence

Number = int | float


class Matrix:
    """Representa uma matriz numérica."""

    def __init__(self, data: Iterable[Iterable[Number]]):
        rows = [list(row) for row in data]

        if not rows:
            raise ValueError("matrix cannot be empty.")

        if not rows[0]:
            raise ValueError("matrix cannot have empty rows.")

        columns = len(rows[0])

        if any(len(row) != columns for row in rows):
            raise ValueError("all rows must have the same length.")

        self._data = rows

    @classmethod
    def zeros(cls, rows: int, columns: int) -> Matrix:
        """Cria uma matriz preenchida com zeros."""
        if rows <= 0 or columns <= 0:
            raise ValueError("rows and columns must be positive.")

        return cls([[0 for _ in range(columns)] for _ in range(rows)])

    @classmethod
    def identity(cls, size: int) -> Matrix:
        """Cria uma matriz identidade."""
        if size <= 0:
            raise ValueError("size must be positive.")

        return cls(
            [
                [1 if row == column else 0 for column in range(size)]
                for row in range(size)
            ]
        )

    @classmethod
    def from_rows(
        cls,
        *rows: Sequence[Number],
    ) -> Matrix:
        """Cria uma matriz a partir de linhas."""
        return cls(rows)

    @property
    def rows(self) -> int:
        return len(self._data)

    @property
    def columns(self) -> int:
        return len(self._data[0])

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @property
    def is_square(self) -> bool:
        return self.rows == self.columns

    def copy(self) -> Matrix:
        return Matrix([row.copy() for row in self._data])

    def to_list(self) -> list[list[Number]]:
        return [row.copy() for row in self._data]

    def transpose(self) -> Matrix:
        return Matrix(
            [
                [self._data[row][column] for row in range(self.rows)]
                for column in range(self.columns)
            ]
        )

    T = property(transpose)

    def row(self, index: int) -> list[Number]:
        return self._data[index].copy()

    def column(self, index: int) -> list[Number]:
        return [self._data[row][index] for row in range(self.rows)]

    def determinant(self) -> Number:
        """Calcula o determinante da matriz."""
        if not self.is_square:
            raise ValueError("determinant is only defined for square matrices.")

        size = self.rows

        if size == 1:
            return self._data[0][0]

        if size == 2:
            return (
                self._data[0][0] * self._data[1][1]
                - self._data[0][1] * self._data[1][0]
            )

        result = 0

        for column in range(size):
            result += self._data[0][column] * self.cofactor(0, column)

        return result

    def minor(self, row: int, column: int) -> Matrix:
        """Retorna a matriz menor removendo uma linha e uma coluna."""
        return Matrix(
            [
                [self._data[r][c] for c in range(self.columns) if c != column]
                for r in range(self.rows)
                if r != row
            ]
        )

    def cofactor(self, row: int, column: int) -> Number:
        """Calcula o cofator de um elemento."""
        sign = -1 if (row + column) % 2 else 1
        return sign * self.minor(row, column).determinant()

    def adjugate(self) -> Matrix:
        """Retorna a matriz adjunta."""
        if not self.is_square:
            raise ValueError("adjugate is only defined for square matrices.")

        return Matrix(
            [
                [self.cofactor(row, column) for row in range(self.rows)]
                for column in range(self.columns)
            ]
        )

    def inverse(self) -> Matrix:
        """Calcula a matriz inversa."""
        determinant = self.determinant()

        if determinant == 0:
            raise ValueError("matrix is singular and cannot be inverted.")

        return self.adjugate() / determinant

    def trace(self) -> Number:
        """Calcula o traço da matriz."""
        if not self.is_square:
            raise ValueError("trace is only defined for square matrices.")

        return sum(self._data[index][index] for index in range(self.rows))

    def map(self, function) -> Matrix:
        """Aplica uma função a cada elemento."""
        return Matrix([[function(value) for value in row] for row in self._data])

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            row, column = key
            self._data[row][column] = value
            return

        if len(value) != self.columns:
            raise ValueError("row must have the same number of columns.")

        self._data[key] = list(value)

    def __iter__(self) -> Iterator[list[Number]]:
        return iter(self._data)

    def __add__(self, other: Matrix) -> Matrix:
        if self.shape != other.shape:
            raise ValueError("matrices must have the same shape.")

        return Matrix(
            [
                [
                    self._data[row][column] + other._data[row][column]
                    for column in range(self.columns)
                ]
                for row in range(self.rows)
            ]
        )

    def __sub__(self, other: Matrix) -> Matrix:
        if self.shape != other.shape:
            raise ValueError("matrices must have the same shape.")

        return Matrix(
            [
                [
                    self._data[row][column] - other._data[row][column]
                    for column in range(self.columns)
                ]
                for row in range(self.rows)
            ]
        )

    def __mul__(self, other: Number | Matrix) -> Matrix:
        if isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError(
                    "matrix dimensions are incompatible for multiplication."
                )

            return Matrix(
                [
                    [
                        sum(
                            self._data[row][k] * other._data[k][column]
                            for k in range(self.columns)
                        )
                        for column in range(other.columns)
                    ]
                    for row in range(self.rows)
                ]
            )

        return self.map(lambda value: value * other)

    def __rmul__(self, other: Number) -> Matrix:
        return self * other

    def __truediv__(self, value: Number) -> Matrix:
        if value == 0:
            raise ZeroDivisionError("cannot divide a matrix by zero.")

        return self.map(lambda element: element / value)

    def __neg__(self) -> Matrix:
        return self * -1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented

        return self._data == other._data

    def __repr__(self) -> str:
        return f"Matrix({self._data!r})"

    def __str__(self) -> str:
        return "\n".join(" ".join(str(value) for value in row) for row in self._data)
