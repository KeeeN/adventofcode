import os
from collections import defaultdict
from functools import reduce
from typing import Any, Set, Tuple

BIG_VAL = 9

Heatmap = dict


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_heatmap(input_path: str) -> Heatmap:
    with open(input_path, "r") as file:
        heatmap = defaultdict(lambda: BIG_VAL)
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                heatmap[(x, y)] = int(c)
    return heatmap


def find_mins(heatmap: Heatmap) -> list[tuple[Any, Any]]:
    def is_min(x, y) -> bool:
        return (
            heatmap[x, y] < heatmap[x + 1, y]
            and heatmap[x, y] < heatmap[x - 1, y]
            and heatmap[x, y] < heatmap[x, y + 1]
            and heatmap[x, y] < heatmap[x, y - 1]
        )

    return list((x, y) for (x, y) in tuple(heatmap.keys()) if is_min(x, y))


def visit(x: int, y: int, visited: Set[Tuple[int, int]], heatmap: Heatmap) -> Set[Tuple[int, int]]:
    visited.add((x, y))
    for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if (i, j) not in visited and heatmap[i, j] < 9:
            visited |= visit(i, j, visited, heatmap)
    return visited


def bassin_size(x: int, y: int, heatmap: Heatmap) -> int:
    return len(visit(x, y, set(), heatmap))


def part_1(input_path: str) -> int:
    heatmap = load_heatmap(input_path)
    return sum(heatmap[x, y] + 1 for x, y in find_mins(heatmap))


def part_2(input_path: str) -> int:
    heatmap = load_heatmap(input_path)
    mins = find_mins(heatmap)
    bassin_sizes = [bassin_size(*pos, heatmap) for pos in mins]
    largest_bassins = list(reversed(sorted(bassin_sizes)))[:3]
    return reduce(lambda x, acc: x * acc, largest_bassins, 1)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
