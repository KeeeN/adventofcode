import os
from typing import List, NewType, Tuple

import numpy as np
from skimage import draw

Line = NewType("Line", Tuple[int, int, int, int])


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def max_table(table: List[List[int]]) -> int:
    return max(map(max, table))


def load_lines(input_path: str) -> Tuple[int, List[Line]]:
    with open(input_path, "r") as file:
        lines = [
            list(map(int, ",".join(line_str.split("->")).split(",")))
            for line_str in file.readlines()
        ]
    return max_table(lines), lines


def is_horizontal_or_vertical(line: Line) -> bool:
    return line[0] == line[2] or line[1] == line[3]


def part_1(input_path: str) -> int:
    max_table, lines = load_lines(input_path)
    table = np.zeros((max_table + 1, max_table + 1))
    for line in filter(is_horizontal_or_vertical, lines):
        rr, cc = draw.line(*line)
        table[rr, cc] += 1
    return np.count_nonzero(table > 1)


def part_2(input_path: str) -> int:
    max_table, lines = load_lines(input_path)
    table = np.zeros((max_table + 1, max_table + 1))
    for line in lines:
        rr, cc = draw.line(*line)
        table[rr, cc] += 1
    return np.count_nonzero(table > 1)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
