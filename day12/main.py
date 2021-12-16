import copy
import functools
import os
from collections import Counter, namedtuple
from itertools import permutations
from typing import Callable, DefaultDict, NamedTuple


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_cave(input_path: str) -> NamedTuple:
    cave_map_mutable = DefaultDict(set)
    with open(input_path, "r") as file:
        for line in file.readlines():
            a, b = line.strip().split("-")
            cave_map_mutable[a].add(b)
            cave_map_mutable[b].add(a)
    cave_map = {k: frozenset(v) for k, v in cave_map_mutable.items()}
    CaveMap = namedtuple("CaveMap", list(cave_map))  # type: ignore
    return CaveMap(**cave_map)  # type: ignore


@functools.cache
def visit(
    cave: str,
    cave_map: NamedTuple,
    visited: tuple,
    get_nexts: Callable[[str, NamedTuple, tuple], set],
):
    visited += (cave,)
    paths = set()
    if cave == "end":
        paths.add(",".join(visited))
        return paths
    nexts = get_nexts(cave, cave_map, visited)
    for perm in permutations(nexts):
        for next_cave in perm:
            paths |= visit(next_cave, cave_map, copy.copy(visited), get_nexts)
    return paths


def part_1(input_path: str) -> int:
    @functools.cache
    def get_nexts(cave: str, cave_map: NamedTuple, visited: tuple) -> set:
        return getattr(cave_map, cave) - set(filter(str.islower, visited))

    cave_map = load_cave(input_path)
    return len(visit("start", cave_map, tuple(), get_nexts))


def part_2(input_path: str) -> int:
    @functools.cache
    def get_nexts(cave: str, cave_map: NamedTuple, visited: tuple) -> set:
        small_caves = list(filter(str.islower, visited))
        visited_twice = [cave for cave, count in Counter(small_caves).items() if count >= 2]
        return (
            getattr(cave_map, cave) - set(small_caves)
            if len(visited_twice) >= 1
            else getattr(cave_map, cave) - set(visited_twice) - {"start"}
        )

    cave_map = load_cave(input_path)
    return len(visit("start", cave_map, tuple(), get_nexts))


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
