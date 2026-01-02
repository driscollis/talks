from functools import wraps
from typing import Any, Callable, TypeVar


Generic_function = TypeVar("Generic_function", bound=Callable[..., Any])

def info(func: Generic_function) -> Generic_function:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('Function name: ' + func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        result = func(*args, **kwargs)
        return result
    return wrapper

@info
def doubler(number: int) -> int:
    """Doubles the number passed to it"""
    return number * 2

print(doubler(4))