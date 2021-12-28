"""Day 7"""
from pathlib import Path
from collections import Counter
from typing import Callable


def mutate(start: str, distfunc: Callable) -> int:
    """Find minimum distance"""
    crabs = Counter(int(x) for x in start.split(","))
    return min(sum(distfunc(k, pos) * v for k, v in crabs.items()) for pos in range(min(crabs), max(crabs) + 1))


def absdist(a: int, b: int) -> int:
    """Absolute distance"""
    return abs(a - b)


def triangledist(a: int, b: int) -> int:
    """Triangle dist between the two points"""
    t = abs(a - b)
    return int(((t + 1) * t) / 2)


if __name__ == "__main__":
    testcase = "16,1,2,0,4,2,7,1,2,14"
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    assert mutate(testcase, absdist) == 37
    print(mutate(data, absdist))

    assert mutate(testcase, triangledist) == 168
    print(mutate(data, triangledist))
