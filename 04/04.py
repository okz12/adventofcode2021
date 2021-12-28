"""Day 4"""
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Tuple, List
from itertools import chain


@dataclass
class board:
    """Bingo board"""

    grid: List[List[int]]
    gridmap: Dict[int, Tuple[int, int]]
    solved: bool = False

    @staticmethod
    def parse(inp: str) -> board:
        """Parse string to board representation"""
        grid = [[int(row[n : n + 2]) for n in range(0, 14, 3)] for row in inp.split("\n")]  # noqa: E203
        gridmap = {grid[y][x]: (y, x) for y in range(len(grid)) for x in range(len(grid[0]))}
        return board(grid, gridmap)

    def check_solved(self, n: int) -> bool:
        """Add a number and see if board wins"""
        if n not in self.gridmap:
            return False
        y, x = self.gridmap[n]

        self.grid[y][x] = -1

        if all(self.grid[y][x_] < 0 for x_ in range(len(self.grid[0]))):
            self.solved = True
            return True
        if all(self.grid[y_][x] < 0 for y_ in range(len(self.grid))):
            self.solved = True
            return True
        return False

    def __repr__(self):
        """Print board"""
        return "\n" + "\n".join(("\t".join(str(x) for x in row) for row in self.grid)) + "\n"


@dataclass
class bingo:
    """Bingo game with boards and numbers announced"""

    nums: List[int]
    boards: List[board]

    @staticmethod
    def parse(inp: str) -> bingo:
        """String to bingo game"""
        nums_s, boards_s = inp.split("\n\n", 1)
        boards = [board.parse(b) for b in boards_s.split("\n\n")]
        nums = [int(x) for x in nums_s.split(",")]
        return bingo(nums, boards)

    def play(self, mode: str = "first") -> int:
        """Play the game and return sum of unmarked numbers times winning number"""
        ret = 0
        for n in self.nums:
            for b in self.boards:
                if not b.solved and b.check_solved(n):
                    ret = sum(x for x in chain.from_iterable(b.grid) if x > 0) * n
                    if mode == "first":
                        return ret
        return ret


if __name__ == "__main__":
    testcase = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7\
 """
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    assert bingo.parse(testcase).play("first") == 4512
    print(bingo.parse(data).play("first"))
    assert bingo.parse(testcase).play("last") == 1924
    print(bingo.parse(data).play("last"))
