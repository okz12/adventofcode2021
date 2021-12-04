from pathlib import Path
from typing import Dict, List

DIRECTION_MAP: Dict[str, complex] = {"forward": 1, "up": 1j, "down": -1j}


def parse_movements(movements: str) -> List[complex]:
    return [DIRECTION_MAP[movement.split(" ")[0]] * int(movement.split(" ")[1]) for movement in movements.split("\n")]


def mult(movements: str) -> int:
    z = sum(parse_movements(movements))
    return abs(int(z.real * z.imag))


def calc_aim(movements: str) -> int:
    moves = parse_movements(movements)
    z = 0j
    aim = 0
    for move in moves:
        aim += int(move.imag)
        if move.real:
            z += move.real + aim * move.real * 1j
    return abs(int(z.real * z.imag))


if __name__ == "__main__":
    testcase = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()
    print(mult(testcase))
    print(mult(data))
    print(calc_aim(testcase))
    print(calc_aim(data))
