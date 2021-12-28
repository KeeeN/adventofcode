import heapq
import os
import sys

sys.setrecursionlimit(int(1e6))


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_map(input_path: str) -> dict:
    with open(input_path, "r") as file:
        risk_map = {
            (x, y): int(v)
            for y, line in enumerate(file.readlines())
            for x, v in enumerate(list(line.strip()))
        }
    return risk_map


ADJ = ((0, 1), (1, 0), (-1, 0), (0, -1))


def next_positions(pos, risk_map, max_width, max_height) -> set[tuple[int, int]]:
    return set(
        (pos[0] + x, pos[1] + y)
        for x, y in ADJ
        if 0 <= pos[0] + x < max_width and 0 <= pos[1] + y < max_height
    )


def visit(pos, risk_counter, risk_map, final_pos):
    if pos == final_pos:
        return
    for next_pos in next_positions(pos, risk_map):
        risk_counter[next_pos] = min(risk_counter[next_pos], risk_counter[pos] + risk_map[next_pos])
        visit(next_pos, risk_counter, risk_map, final_pos)


def get_closest(risk_counter, visited) -> tuple[int, int]:
    not_visited = filter(lambda e: e[0] not in visited, risk_counter.items())
    return min(not_visited, key=lambda e: e[1])[0]


def visit_2(pos, risk_counter, risk_map, final_pos, max_width, max_height, visited: set = None):
    if visited is None:
        visited = set()
    # Dijkstra
    visited.add(pos)
    if pos == final_pos:
        return
    for next_pos in next_positions(pos, risk_map, max_width, max_height) - visited:
        risk_counter[next_pos] = min(risk_counter[next_pos], risk_counter[pos] + risk_map[next_pos])
    visit_2(
        pos=get_closest(risk_counter, visited),
        risk_counter=risk_counter,
        risk_map=risk_map,
        final_pos=final_pos,
        max_width=max_width,
        max_height=max_height,
        visited=visited,
    )


def visit_3(
    pos,
    risk_counter,
    risk_map,
    final_pos,
    max_width,
    max_height,
    visited: set = None,
    candidates: list = None,
):
    if visited is None:
        visited = set()
    if candidates is None:
        candidates = list()
    # Dijkstra
    while candidates or pos == (0, 0):
        visited.add(pos)
        if pos == final_pos:
            return
        for next_pos in next_positions(pos, risk_map, max_width, max_height) - visited:
            if (next_risk := risk_counter[pos] + risk_map[next_pos]) < risk_counter[next_pos]:
                risk_counter[next_pos] = next_risk
                heapq.heappush(candidates, (next_risk, *next_pos))
        _, x, y = heapq.heappop(candidates)
        pos = (x, y)


def find_path(risk_map):
    pos = (0, 0)
    width, height = map_size(risk_map)
    final_pos = width - 1, height - 1
    risk_counter = {
        (x, y): width * height * 9 for x in range(final_pos[0] + 1) for y in range(final_pos[1] + 1)
    }
    risk_counter[pos] = 0
    visit_3(pos, risk_counter, risk_map, final_pos, width, height)
    return risk_counter, final_pos


def map_size(risk_map: dict) -> tuple[int, int]:
    return (
        max(risk_map.keys(), key=lambda pos: pos[0])[0] + 1,
        max(risk_map.keys(), key=lambda pos: pos[1])[1] + 1,
    )


def part_1(input_path: str) -> int:
    risk_map = load_map(input_path)
    risk_counter, final_pos = find_path(risk_map)
    return risk_counter[final_pos]


def scale_map(risk_map: dict, factor: int) -> dict:
    width, height = map_size(risk_map)
    return {
        (x + width * i, y + height * j): (v + i + j) - 9 * ((v + i + j) // 10)
        for (x, y), v in risk_map.items()
        for i in range(factor)
        for j in range(factor)
    }


def display_map(risk_map: dict) -> None:
    width, height = map_size(risk_map)
    for y in range(height):
        print("".join(str(risk_map[(x, y)]) for x in range(width)))


def display_counter(risk_counter, risk_map) -> None:
    width, height = map_size(risk_map)
    for y in range(height):
        print(" ".join(f"{risk_counter[(x, y)]:02}" for x in range(width)))


def part_2(input_path: str) -> int:
    risk_map = load_map(input_path)
    risk_map = scale_map(risk_map, 5)
    risk_counter, final_pos = find_path(risk_map)
    return risk_counter[final_pos]


if __name__ == "__main__":
    import timeit

    input_path = get_local_file_abs_path("input.txt")
    print(timeit.timeit("part_1(input_path)", globals=globals(), number=1))
    print(timeit.timeit("part_2(input_path)", globals=globals(), number=1))
    print(part_1(input_path))
    print(part_2(input_path))
