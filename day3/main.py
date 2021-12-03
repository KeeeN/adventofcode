import os
from typing import List


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)

def list_int_to_decimal(list_int: List[int]) -> int:
    return int("".join(map(str, list_int)), base=2)

def part_1() -> int:
    with open(get_local_file_abs_path("input.txt"), "r") as file:
        sum_list = [0] * 12
        line_count = 0
        for line in file.readlines():
            line_iter = map(int, list(line.strip("\n")))
            sum_list = [a + b for a, b in zip(sum_list, line_iter)]
            line_count += 1
    epsilon = []
    gamma = []
    for elem in sum_list:
        epsilon.append(1 if elem > line_count / 2 else 0)
        gamma.append(1 if elem < line_count / 2 else 0)
    epsilon = list_int_to_decimal(epsilon)
    gamma = list_int_to_decimal(gamma)
    return epsilon * gamma


if __name__ == "__main__":
    print(part_1())