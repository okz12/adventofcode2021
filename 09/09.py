"""Day 9"""
from pathlib import Path
from typing import List, Callable
from math import prod


def basin_size(grid: List[List[int]], x_init: int, y_init: int) -> int:
    """Finds basin size at x, y"""
    stack = [(y_init, x_init)]
    visited = set()
    while stack:
        y, x = stack.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_, y_ = x + dx, y + dy
            if (0 <= y_ < len(grid)) and (0 <= x_ < len(grid[0])) and (grid[y_][x_] != 9) and ((y_, x_) not in visited):
                stack.append((y_, x_))
        visited.add((y, x))
    return len(visited)


def add1(grid: List[List[int]], x: int, y: int) -> int:
    """Adds one to value"""
    return grid[y][x] + 1


def prod_3_largest(points: List[int]) -> int:
    """Product of 3 largest points"""
    return prod(sorted(points, reverse=True)[:3])


def calc_lp(grids: str, value_func: Callable, collate_func: Callable) -> int:
    """Calculate lowest points"""
    grid = [[int(x) for x in row] for row in grids.split("\n")]
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if all(
                not ((0 <= x + dx < len(grid[0])) and (0 <= y + dy < len(grid))) or grid[y][x] < grid[y + dy][x + dx]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ):
                low_points.append(value_func(grid, x, y))
    return collate_func(low_points)


if __name__ == "__main__":
    testcase = """\
2199943210
3987894921
9856789892
8767896789
9899965678\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    assert calc_lp(testcase, add1, sum) == 15
    print(calc_lp(data, add1, sum))

    assert calc_lp(testcase, basin_size, prod_3_largest) == 1134
    print(calc_lp(data, basin_size, prod_3_largest))
