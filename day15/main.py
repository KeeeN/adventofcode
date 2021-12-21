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


def next_positions(pos, risk_map) -> set[tuple[int, int]]:
    return set(
        (pos[0] + x, pos[1] + y) for x, y in ADJ if (pos[0] + x, pos[1] + y) in risk_map.keys()
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


def visit_2(pos, risk_counter, risk_map, final_pos, visited: set = set()):
    # Dijkstra
    visited.add(pos)
    if pos == final_pos:
        return
    for next_pos in next_positions(pos, risk_map) - visited:
        risk_counter[next_pos] = min(risk_counter[next_pos], risk_counter[pos] + risk_map[next_pos])
    visit_2(get_closest(risk_counter, visited), risk_counter, risk_map, final_pos, visited)


def part_1(input_path: str) -> int:
    risk_map = load_map(input_path)
    pos = (0, 0)
    final_pos = (
        max(risk_map.keys(), key=lambda pos: pos[0])[0],
        max(risk_map.keys(), key=lambda pos: pos[1])[1],
    )
    risk_counter = {
        (x, y): (final_pos[0] + final_pos[1]) * 9
        for x in range(final_pos[0] + 1)
        for y in range(final_pos[1] + 1)
    }
    risk_counter[pos] = 0
    visit_2(pos, risk_counter, risk_map, final_pos)
    return risk_counter[final_pos]


def part_2(input_path: str) -> int:
    risk_map = load_map(input_path)
    return risk_map


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
