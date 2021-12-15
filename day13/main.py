import os
from functools import reduce
from statistics import median


PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

SCORES_2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_chunks(input_path: str) -> list[str]:
    with open(input_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def part_1(input_path: str) -> int:
    chunks = load_chunks(input_path)
    score = 0
    for chunk in chunks:
        opened: list[str] = []
        for c in chunk:
            if opened is not None and c in PAIRS.keys():
                if PAIRS[c] != opened[-1]:
                    score += SCORES[c]
                    break
                else:
                    opened.pop()
            else:
                opened.append(c)
    return score


def part_2(input_path: str) -> int:
    chunks = load_chunks(input_path)
    scores = []
    for chunk in chunks:
        opened: list[str] = []
        skip_chunk = False
        for c in chunk:
            if opened is not None and c in PAIRS.keys():
                if PAIRS[c] != opened[-1]:
                    skip_chunk = True
                    break
                else:
                    opened.pop()
            else:
                opened.append(c)
        if skip_chunk:
            continue
        if len(opened) > 0:
            scores.append(
                reduce(lambda acc, x: acc * 5 + x, (SCORES_2[c] for c in opened[::-1]), 0)
            )
    return int(median(scores))


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
