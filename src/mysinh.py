from decimal import Decimal, setcontext, Context, ROUND_HALF_EVEN
from typing import Optional
from math import pow

import math

DEFAULT_NUM_ITERATIONS = 50
DEFAULT_PRECISION = 30


def factorial(n: int) -> int:
    result = int(1)
    for i in range(1, n + 1):
        result *= i
    return result


def sinh(
    x: float,
    number_of_iterations: Optional[int] = None,
    precision: Optional[int] = None,
) -> Decimal:
    result = Decimal(0)
    precision = DEFAULT_PRECISION if not precision else precision

    setcontext(Context(prec=precision, rounding=ROUND_HALF_EVEN))
    iterations = (
        number_of_iterations if number_of_iterations else DEFAULT_NUM_ITERATIONS
    )
    if x == 0:
        return 0
    for n in range(0, iterations):
        result += (Decimal(x) ** (Decimal(2) * Decimal(n))) / Decimal(factorial(2 * n))
    return result


def test_sinh(print_results: Optional[bool] = None):
    for i in range(0, 100):
        if print_results:
            print(f"{sinh(i)} = mysinh({i}) | {math.sinh(i)} = math.sinh({i})")


def test_factorial(print_results: Optional[bool] = None):
    for i in range(0, 100):
        assert math.factorial(i) == factorial(i)
        if print_results:
            print(f"{int(factorial(i))} | {math.factorial(i)}")
