from functools import lru_cache
from typing import Generator


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_alt(n: int) -> int:
    if n == 0:
        return n
    lst: int = 0
    nxt: int = 1
    for _ in range(1, n):
        lst, nxt = nxt, lst + nxt
    return nxt


def fib_iter(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    lst: int = 0
    nxt: int = 1
    for _ in range(1, n):
        lst, nxt = nxt, lst + nxt
        yield nxt


if __name__ == "__main__":
    x = fib(5)
    y = fib(50)
    z = fib_alt(50)
    print(x, y, z)
    for i in fib_iter(50):
        print(i)
