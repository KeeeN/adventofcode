import os
import re

Target = dict[str, int]
Vel = tuple[int, int]
Pos = tuple[int, int]


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_target(input_path: str) -> Target:
    line = open(input_path, "r").readline().strip()
    result = re.search(
        r"x=(?P<x_min>-?\d+)\.{2}(?P<x_max>-?\d+), y=(?P<y_min>-?\d+)\.{2}(?P<y_max>-?\d+)", line
    ).groupdict()
    return {k: int(v) for k, v in result.items()}


def move(pos: Pos, vel: Vel) -> tuple[tuple[int, int], tuple[int, int]]:
    p_x, p_y = pos[0] + vel[0], pos[1] + vel[1]
    v_x = vel[0] - 1 if vel[0] > 0 else vel[0] + 1 if vel[0] < 0 else 0
    v_y = vel[1] - 1
    return (p_x, p_y), (v_x, v_y)


def target_missed(target: Target, pos: Pos) -> bool:
    return pos[0] > target["x_max"] or pos[1] < target["y_min"]


def target_reached(target: Target, pos: Pos) -> bool:
    return (
        target["x_min"] <= pos[0] <= target["x_max"]
        and target["y_min"] <= pos[1] <= target["y_max"]
    )


def launch(pos: Pos, vel: Vel, target: Target) -> tuple[bool, int]:
    highest = pos[1]
    while not target_missed(target, pos) and not (reached := target_reached(target, pos)):
        pos, vel = move(pos, vel)
        highest = max(highest, pos[1])
    return reached, highest


def part_1(input_path: str) -> int:
    target = load_target(input_path)
    highests = []
    for vel_x in range(100):
        for vel_y in range(-30, 500):
            reached, highest = launch((0, 0), (vel_x, vel_y), target)
            if reached:
                highests.append(highest)
    return max(highests)


def part_2(input_path: str) -> int:
    return load_target(input_path)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
