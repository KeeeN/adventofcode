import os
from typing import Tuple


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def move(x: int, depth: int, instruction: str) -> Tuple[int, int]:
    match instruction.split():
        case ["forward", value]:
            x += int(value)
        case ["up", value]:
            depth = max(0, depth - int(value))
        case ["down", value]:
            depth += int(value)
    return x, depth


def part_1() -> int:
    with open(get_local_file_abs_path("input.txt"), "r") as file:
        x, depth = 0, 0
        for instruction in file.readlines():
            x, depth = move(x, depth, instruction)
    return x * depth


def move_2(x: int, depth: int, aim: int, instruction: str) -> Tuple[int, int]:
    match instruction.split():
        case ["forward", value]:
            x += int(value)
            depth += int(value) * aim
        case ["up", value]:
            aim -= int(value)
        case ["down", value]:
            aim += int(value)
    return x, depth, aim


def part_2() -> int:
    with open(get_local_file_abs_path("input.txt"), "r") as file:
        x, depth, aim = 0, 0, 0
        for instruction in file.readlines():
            x, depth, aim = move_2(x, depth, aim, instruction)
    return x * depth


if __name__ == "__main__":
    print(part_1())
    print(part_2())
