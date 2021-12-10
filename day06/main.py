import os
from collections import Counter
from typing import List, NewType, Tuple


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_fishes(input_path: str) -> List[int]:
    with open(input_path, "r") as file:
        counter = Counter(list(map(int, file.readline().split(","))))
        return [counter[i] for i in range(9)]


def part_1(input_path: str, days: int) -> int:
    fishes = load_fishes(input_path)
    for _ in range(days):
        new_fishes_count = fishes.pop(0)
        fishes.append(new_fishes_count)
        fishes[6] += new_fishes_count
    return sum(fishes)


def part_2(input_path: str, days: int) -> int:
    return part_1(input_path, days)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path, 80))
    print(part_1(input_path, 256))
