""""
Automatic memoization
"""


from functools import lru_cache

@lru_cache
def fib4(n: int) -> int: # Same definition as fib2()
    if n < 2: # base case
        return n
    return fib4(n - 2) + fib4(n - 1) # Recursive case

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))