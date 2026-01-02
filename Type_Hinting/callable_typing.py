from typing import Callable

def adder(a: int, b: int) -> int:
    return a + b

def caller() -> Callable[[int, int], int]:
    return adder

c = caller()
c(1, 2)