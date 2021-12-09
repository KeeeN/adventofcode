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
    median = int(statistics.median(crabes))
    return sum(map(lambda x: abs(x - median), crabes))


def part_2(input_path: str) -> int:
    def calc_fuel(target_pos: int, pos: int) -> int:
        dist = abs(pos - target_pos)
        return int(dist * (dist + 1) // 2)

    def calc_total_fuel(crabes: List[int], target_pos: int) -> int:
        return sum(map(lambda pos: calc_fuel(target_pos, pos), crabes))

    crabes = load_crabes(input_path)
    fuel_list = [
        calc_total_fuel(crabes, target_pos) for target_pos in range(min(crabes), max(crabes))
    ]
    return min(fuel_list)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
