"""Day 3"""
from typing import List
from copy import deepcopy
from pathlib import Path


def find_consumption(inp: str) -> int:
    """Part 1"""
    transpose = list(zip(*[[int(x) for x in list(row)] for row in inp.split("\n")]))
    nums = [1 if row.count(1) >= len(row) / 2 else 0 for row in transpose]
    gamma = int("".join(str(x) for x in nums), 2)
    epsilon = int("".join(str(1 - x) for x in nums), 2)
    return gamma * epsilon


def filt(grid: List[List[int]], mcb: int) -> int:
    """Filter grid rows using the most common bit"""
    for x in range(len(grid[0])):
        most_common_bit = mcb if sum(row[x] for row in grid) >= len(grid) / 2 else 1 - mcb
        for y in range(len(grid) - 1, -1, -1):
            if grid[y][x] != most_common_bit:
                grid.pop(y)
        if len(grid) == 1:
            return int("".join(str(x) for x in grid[0]), 2)
    return int("".join(str(x) for x in grid[0]), 2)


def find_rating(inp: str) -> int:
    """Part 2"""
    grid = [[int(x) for x in list(row)] for row in inp.split("\n")]
    o2, co2 = filt(deepcopy(grid), 1), filt(deepcopy(grid), 0)
    return o2 * co2


if __name__ == "__main__":
    testcase = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()
    print(find_consumption(testcase))
    print(find_consumption(data))
    print(find_rating(testcase))
    print(find_rating(data))
