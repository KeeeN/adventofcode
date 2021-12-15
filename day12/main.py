import copy
import functools
import os
from collections import namedtuple
from itertools import permutations
from typing import DefaultDict


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_cave(input_path: str) -> namedtuple:
    cave_map = DefaultDict(set)
    with open(input_path, "r") as file:
        for line in file.readlines():
            a, b = line.strip().split("-")
            cave_map[a].add(b)
            cave_map[b].add(a)
    cave_map = {k: frozenset(v) for k, v in cave_map.items()}
    CaveMap = namedtuple("CaveMap", cave_map)
    return CaveMap(**cave_map)


@functools.cache
def visit(cave: str, cave_map: namedtuple, visited: tuple):
    visited += (cave,)
    paths = set()
    if cave == "end":
        paths.add(",".join(visited))
        return paths
    nexts = getattr(cave_map, cave) - set(filter(str.islower, visited))
    for perm in permutations(nexts):
        for next_cave in perm:
            paths |= visit(next_cave, cave_map, copy.copy(visited))
    return paths


def part_1(input_path: str) -> int:
    cave_map = load_cave(input_path)
    return len(visit("start", cave_map, tuple()))


def part_2(input_path: str) -> int:
    cave_map = load_cave(input_path)
    return len(visit("start", cave_map, tuple()))


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
