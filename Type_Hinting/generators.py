from typing import Iterator, Generator

# Simple generator that only yields integers
def infinite_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1

# More complex generator that accepts sent values and returns a final value
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent:
        sent = yield round(sent)
    return 'Done'
