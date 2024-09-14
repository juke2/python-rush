from typing import Optional

fib_dict = {0: 0, 1: 1}


def fibonacci(x: int) -> int:
    fib_of_i_minus_1 = 1
    fib_of_i_minus_2 = 0
    result = x
    for i in range(1, x):
        result = fib_of_i_minus_1 + fib_of_i_minus_2
        fib_of_i_minus_2 = fib_of_i_minus_1
        fib_of_i_minus_1 = result
    return result


def fibonacci_recursive(x: int) -> int:
    if x in fib_dict.keys():
        return fib_dict[x]
    result = fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)
    fib_dict[x] = result
    return result


def test_fibonacci(print_results: Optional[bool] = None) -> None:
    for i in range(0, 100):
        assert fibonacci(i) == fibonacci_recursive(i)
        if print_results:
            print(f"{fibonacci(i)} = fib({i}) | {fibonacci_recursive(i)} = rfib({i})")
