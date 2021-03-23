from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

factorial(10)
factorial(5)
factorial(15)