def is_even(value: int) -> bool:
    return value % 2 == 0


def is_odd(value: int) -> bool:
    return value % 2 != 0


def is_prime(value: int) -> bool:
    if value < 2:
        return False

    if value == 2:
        return True

    if value % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= value:
        if value % divisor == 0:
            return False

        divisor += 2

    return True


def factorial(value: int) -> int:
    if value < 0:
        raise ValueError("factorial is not defined for negative numbers.")

    result = 1

    for number in range(2, value + 1):
        result *= number

    return result
