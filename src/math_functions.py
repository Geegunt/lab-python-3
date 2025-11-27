def factorial_recurs(n: int) -> int:
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recurs(n - 1)

def factorial_default(n: int) -> int:
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k


def fib_recurs(n: int) -> int:
    if n < 0:
        raise ValueError("n не должно быть отрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recurs(n - 1) + fib_recurs(n - 2)

def fib_default(n: int) -> int:
    x0 = 1
    x1 = 1
    x2 = 0
    for i in range(2, a):
        x2 = x1 + x0
        x0 = x1
        x1 = x2
    return x1

print(factorial_recurs(5))
print(factorial_default(5))
print(fib_recurs(5))
print(fib_default(5))