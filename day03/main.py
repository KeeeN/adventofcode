import os
from collections.abc import Callable
from typing import List, Tuple

SIZE = 12


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def list_int_to_str(list_int: List[int]) -> str:
    return "".join(map(str, list_int))


def calc_epsilon_gamma(line_list: List[str]) -> Tuple[str, str]:
    sum_list = [0] * SIZE
    line_count = len(line_list)
    for line in line_list:
        line_iter = map(int, list(line.strip("\n")))
        sum_list = [a + b for a, b in zip(sum_list, line_iter)]
    epsilon_list = []
    gamma_list = []
    for elem in sum_list:
        epsilon_list.append(1 if elem >= line_count / 2 else 0)
        gamma_list.append(1 if elem < line_count / 2 else 0)
    return list_int_to_str(epsilon_list), list_int_to_str(gamma_list)


def calc_epsilon(line_list: List[str]) -> str:
    return calc_epsilon_gamma(line_list)[0]


def calc_gamma(line_list: List[str]) -> str:
    return calc_epsilon_gamma(line_list)[1]


def part_1(input_path: str) -> Tuple[int, str, str]:
    with open(input_path, "r") as file:
        line_list = file.readlines()
        epsilon_str, gamma_str = calc_epsilon_gamma(line_list)
    epsilon_int = int(epsilon_str, base=2)
    gamma_int = int(gamma_str, base=2)
    return epsilon_int * gamma_int, epsilon_str, gamma_str


def part_2(input_path: str) -> Tuple[int, str, str]:
    def filter_numbers_pos(numbers: List[str], mask: str, pos: int) -> List[str]:
        return list(filter(lambda line: line[pos] == mask[pos], numbers))

    def filter_numbers(numbers: List[str], calc_fun: Callable[[list], str]) -> str:
        numbers_ = numbers.copy()
        for pos in range(SIZE):
            numbers_ = filter_numbers_pos(numbers_, calc_fun(numbers_), pos)
            if len(numbers_) == 1:
                break
        return numbers_[0]

    def calc_oxygen_rating(numbers) -> str:
        return filter_numbers(numbers, calc_epsilon)

    def calc_co2_rating(numbers) -> str:
        return filter_numbers(numbers, calc_gamma)

    with open(input_path, "r") as file:
        numbers = [line.strip("\n") for line in file.readlines()]

    oxygen_rating_str = calc_oxygen_rating(numbers)
    co2_rating_str = calc_co2_rating(numbers)
    oxygen_rating_int = int(oxygen_rating_str, base=2)
    co2_rating_int = int(co2_rating_str, base=2)
    return oxygen_rating_int * co2_rating_int, oxygen_rating_str, co2_rating_str


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
