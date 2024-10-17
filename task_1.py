from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a function to calculate fibonacci number which uses cache to optimize calculations
    """

    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if not n in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci
