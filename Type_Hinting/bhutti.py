import time
from collections.abc import Callable
from functools import wraps

def measure_execution_time[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    # Preserve function metadata with wraps
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} s")
        return result
    return wrapper

@measure_execution_time
def slow_function() -> None:
    time.sleep(1)

slow_function()