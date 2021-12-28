"""Day 6"""
from pathlib import Path
from collections import Counter


def mutate(start: str, n_days: int) -> int:
    """Simulate for n_days the count of laternfish evolving"""
    fish = Counter(int(x) for x in start.split(","))
    for x in range(9):
        if x not in fish:
            fish[x] = 0

    for _ in range(n_days):
        fish6, fish7, fish8 = fish[7] + fish[0], fish[8], fish[0]
        for n in range(6):
            fish[n] = fish[n + 1]
        fish[6], fish[7], fish[8] = fish6, fish7, fish8

    return sum(fish.values())


if __name__ == "__main__":
    testcase = "3,4,3,1,2"
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    assert mutate(testcase, 80) == 5934
    print(mutate(data, 80))
    assert mutate(testcase, 256) == 26984457539
    print(mutate(data, 256))
