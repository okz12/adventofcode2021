"""Day 8"""
from pathlib import Path
from collections import Counter
from typing import Dict

SEG7: Dict[str, str] = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def decode_7seg(line: str) -> int:
    """Step by step find each segment and decode each number"""
    decode, encoded = line.split(" | ")
    c = Counter(decode)
    del c[" "]
    dig1 = [x for x in decode.split(" ") if len(x) == 2][0]
    dig4 = [x for x in decode.split(" ") if len(x) == 4][0]
    dig7 = [x for x in decode.split(" ") if len(x) == 3][0]
    dig8 = [x for x in decode.split(" ") if len(x) == 7][0]
    segmap = {}
    segmap["b"] = [k for k, v in c.most_common() if v == 6][0]  # occurs 6 times in 7seg
    segmap["e"] = [k for k, v in c.most_common() if v == 4][0]  # occurs 4 times in 7seg
    segmap["f"] = [k for k, v in c.most_common() if v == 9][0]  # occurs 9 times in 7seg
    segmap["a"] = (set(dig7) - set(dig1)).pop()  # occurs in digit 7 but not 1
    segmap["c"] = ({k for k, v in c.most_common() if v == 8} - {segmap["a"]}).pop()  # occurs 8 times but not segmap'a'
    segmap["g"] = (set(dig8) - set(dig4) - {segmap["a"], segmap["e"]}).pop()  # digit 8 segs - digit 4 segs - a, e
    segmap["d"] = (set("abcdefg") - set(segmap.values())).pop()  # remaining segment
    segmapinv = {v: k for k, v in segmap.items()}
    return int("".join([SEG7["".join(sorted(segmapinv[ch] for ch in list(word)))] for word in encoded.split(" ")]))


if __name__ == "__main__":
    testcase = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\
"""
    with open(Path(__file__).parent / "input.txt", "r") as f:
        data = f.read()
    assert (
        sum(sum(1 for x in line.split(" | ")[1].split(" ") if len(x) in {2, 3, 4, 7}) for line in testcase.split("\n"))
        == 26
    )
    print(sum(sum(1 for x in line.split(" | ")[1].split(" ") if len(x) in {2, 3, 4, 7}) for line in data.split("\n")))

    assert sum(decode_7seg(line) for line in testcase.split("\n")) == 61229
    print(sum(decode_7seg(line) for line in data.split("\n")))
