def fib1(n: int) -> int:
    """
    Have a problem
    becouse have a infinite loop.
    """
    return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(5))
    