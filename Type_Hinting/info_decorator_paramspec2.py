from functools import wraps
from typing import Callable


def info[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print('Function name: ' + func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        return func(*args, **kwargs)
    return wrapper

@info
def doubler(number: int) -> int:
    """Doubles the number passed to it"""
    return number * 2

print(doubler(4))