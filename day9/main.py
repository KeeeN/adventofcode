from functools import reduce
import os
from typing import List, NewType, Set, Tuple

BIG_VAL = 10

Heatmap = NewType("Heatmap", List[List[int]])


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_heatmap(input_path: str) -> Heatmap:
    with open(input_path, "r") as file:
        heatmap = [
            [BIG_VAL] + [int(c) for c in line.strip("\n")] + [BIG_VAL]
            for line in file.readlines()
        ]
    height = len(heatmap)
    width = len(heatmap[0]) - 2
    heatmap.insert(0, [BIG_VAL] * (width + 2))
    heatmap.append([BIG_VAL] * (width + 2))
    return heatmap, width, height


def find_mins(heatmap: Heatmap, width: int, height: int) -> int:
    def is_min(x, y) -> bool:
        return (
            heatmap[y][x] < heatmap[y - 1][x]
            and heatmap[y][x] < heatmap[y + 1][x]
            and heatmap[y][x] < heatmap[y][x - 1]
            and heatmap[y][x] < heatmap[y][x + 1]
        )

    return list(
        (x, y)
        for y in range(1, height + 1)
        for x in range(1, width + 1)
        if is_min(x, y)
    )


def visit(
    x: int, y: int, visited: Set[Tuple[int, int]], heatmap: Heatmap
) -> Set[Tuple[int, int]]:
    visited.add((x, y))
    for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if (i, j) not in visited and heatmap[j][i] < 9:
            visited |= visit(i, j, visited, heatmap)
    return visited


def bassin_size(x: int, y: int, heatmap: Heatmap) -> int:
    return len(visit(x, y, set(), heatmap))


def part_1(input_path: str) -> int:
    heatmap, width, height = load_heatmap(input_path)
    return sum(heatmap[y][x] + 1 for x, y in find_mins(heatmap, width, height))


def part_2(input_path: str) -> int:
    heatmap, width, height = load_heatmap(input_path)
    mins = find_mins(heatmap, width, height)
    bassin_sizes = [bassin_size(*pos, heatmap) for pos in mins]
    largest_bassins = list(reversed(sorted(bassin_sizes)))[:3]
    return reduce(lambda x, acc: x * acc, largest_bassins, 1)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
