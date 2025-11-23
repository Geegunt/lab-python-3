def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

