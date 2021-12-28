"""Day 5"""
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from typing import List
from collections import Counter, defaultdict
from itertools import chain


@dataclass
class Line:
    """Generate all points on the line from start to end"""

    start: complex
    end: complex
    direction: complex

    @staticmethod
    def parse(line: str) -> Line:
        """Parse start and end points from each line"""
        p1s, p2s = line.split(" -> ")
        start = int(p1s.split(",")[0]) + int(p1s.split(",")[1]) * (1j)
        end = int(p2s.split(",")[0]) + int(p2s.split(",")[1]) * (1j)
        direction = (end - start) / (max(abs(end.real - start.real), abs(end.imag - start.imag)))
        return Line(start, end, direction)

    def generate_points(self, mode: str = "") -> List[complex]:
        """Output list of points on the line"""
        if mode != "diag" and (self.direction.imag and self.direction.real):
            return []
        start = self.start
        points = [start]
        while start != self.end:
            start += self.direction
            points.append(start)
        return points


@dataclass
class Grid2D:
    """2D Grid of lines"""

    lines: List[Line]

    @staticmethod
    def parse(grid: str) -> Grid2D:
        """Parse each line"""
        return Grid2D([Line.parse(line) for line in grid.split("\n")])

    def simulate(self, mode: str = "") -> int:
        """Simulate drawing up of each line and counting points with more than one occurrence"""
        points = Counter(chain.from_iterable(line.generate_points(mode) for line in self.lines))
        point_counts = defaultdict(list)
        for k, v in points.items():
            point_counts[v].append(k)
        del point_counts[1]
        return sum(map(len, point_counts.values()))


if __name__ == "__main__":
    testcase = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    assert Grid2D.parse(testcase).simulate() == 5
    print(Grid2D.parse(data).simulate())

    assert Grid2D.parse(testcase).simulate("diag") == 12
    print(Grid2D.parse(data).simulate("diag"))
