"""Day 10"""
from pathlib import Path
from typing import Dict

BRACKET_MAP: Dict[str, str] = {"<": ">", "(": ")", "[": "]", "{": "}"}

BRACKET_POINTS: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}

BRACKET_COMPL_POINTS: Dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}


def is_valid(line: str) -> int:
    """Calculate valid score"""
    stack = []
    for br in list(line):
        if br in BRACKET_MAP:
            stack.append(br)
        elif stack and BRACKET_MAP[stack[-1]] == br:
            stack.pop()
        else:
            return BRACKET_POINTS[br]
    return 0


def compl_score(line: str) -> int:
    """Calculate string completion score"""
    if is_valid(line):
        return 0

    stack = []
    for br in list(line):
        if br in BRACKET_MAP:
            stack.append(br)
        elif stack and BRACKET_MAP[stack[-1]] == br:
            stack.pop()

    score = 0
    while stack:
        score = score * 5 + BRACKET_COMPL_POINTS[BRACKET_MAP[stack.pop()]]
    return score


def compl_score_case(case: str) -> int:
    """Wrapper to get completion score middle score"""
    scores = [compl_score(line) for line in case.split("\n")]
    scores = [x for x in scores if x > 0]
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    testcase = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()

    assert sum(is_valid(line) for line in testcase.split("\n")) == 26397
    print(sum(is_valid(line) for line in data.split("\n")))

    assert compl_score_case(testcase) == 288957
    print(compl_score_case(data))
