import os
import statistics
from typing import List


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_crabes(input_path: str) -> List[int]:
    with open(input_path, "r") as file:
        return list(map(int, file.readline().split(",")))


def part_1(input_path: str) -> int:
    crabes = load_crabes(input_path)
    mean = statistics.mean(crabes)
    median = statistics.median(crabes)
    return sum(map(lambda x: abs(x - median), crabes))


def part_2(input_path: str) -> int:
    return part_1(input_path)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_1(input_path))
