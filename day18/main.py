import os
import re
import sys
from functools import reduce
from itertools import permutations

sys.setrecursionlimit(int(1e6))


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_operands(input_path: str) -> list[str]:
    with open(input_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def snail_explode(sn: str, start_pos: int) -> str:
    end_pos = sn.find("]", start_pos) + 1
    a, b = eval(sn[start_pos:end_pos])
    part_1 = re.sub(
        r"\d+", lambda m: str(int(m.group(0)[::-1]) + a)[::-1], sn[:start_pos][::-1], 1
    )[::-1]
    part_2 = re.sub(r"\d+", lambda m: str(int(m.group(0)) + b), sn[end_pos:], 1)
    return part_1 + "0" + part_2


def snail_split(sn: str) -> str:
    return re.sub(
        r"\d{2}", lambda m: f"[{int(m.group(0))//2},{int(m.group(0)) - int(m.group(0))//2}]", sn, 1
    )


def snail_reduce(sn: str) -> str:
    depth = 0
    for pos, s in enumerate(sn):
        if s == "[":
            depth += 1
            if depth == 5:
                return snail_explode(sn, pos)
            continue
        if s == "]":
            depth -= 1
            continue
    return snail_split(sn)


def snail_add(sn_1: str, sn_2: str) -> str | None:
    if sn_1 is None and sn_2:
        return sn_2
    if sn_1 and sn_2 is None:
        return sn_1
    if sn_1 is None and sn_2 is None:
        return None
    before = None
    reduced = f"[{sn_1},{sn_2}]"
    while before != reduced:
        before, reduced = reduced, snail_reduce(reduced)
    return reduced


def calc_magnitude(sn: list) -> int:
    a = sn[0] if type(sn[0]) is int else calc_magnitude(sn[0])
    b = sn[1] if type(sn[1]) is int else calc_magnitude(sn[1])
    return 3 * a + 2 * b


def part_1(input_path: str) -> int:
    operands = load_operands(input_path)
    sn = reduce(lambda acc, val: snail_add(acc, val), operands, None)
    sn_list = eval(sn)
    return calc_magnitude(sn_list)


def part_2(input_path: str) -> int:
    operands = load_operands(input_path)
    perms = permutations(operands, 2)
    results = [calc_magnitude(eval(snail_add(a, b))) for a, b in perms]
    return max(results)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
