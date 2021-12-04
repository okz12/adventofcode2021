"""Day 1"""
from pathlib import Path
from typing import List


def count_depth_increase(depths: List[int]) -> int:
    """Part 1"""
    return sum(depths[n + 1] > depths[n] for n in range(len(depths) - 1))


def sliding_window_3(depths: List[int]) -> List[int]:
    """Create sliding window summation for Part 2"""
    return [depths[n] + depths[n + 1] + depths[n + 2] for n in range(len(depths) - 2)]


if __name__ == "__main__":
    testcase = """\
199
200
208
210
200
207
240
269
260
263\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    testcase_nums = [int(x) for x in testcase.split()]
    data_nums = [int(x) for x in data.split()]
    print(count_depth_increase(testcase_nums))
    print(count_depth_increase(data_nums))
    print(count_depth_increase(sliding_window_3(testcase_nums)))
    print(count_depth_increase(sliding_window_3(data_nums)))
