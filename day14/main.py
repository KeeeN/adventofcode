import functools
import os
from collections import namedtuple
from typing import Counter, NamedTuple


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_polymer(input_path: str) -> tuple[str, NamedTuple]:
    with open(input_path, "r") as file:
        lines = file.readlines()
        rules = dict([tuple(line.strip().split(" -> ")) for line in lines[2:]])
        Rules = namedtuple("Rules", rules)
        return lines[0].strip(), Rules(**rules)


@functools.cache
def apply_step(polymer: str, rules: NamedTuple) -> str:
    new_polymer = ""
    for c1, c2 in zip(polymer, polymer[1:] + "0"):
        new_polymer += c1 + getattr(rules, c1 + c2, "")
    return new_polymer


def part_1(input_path: str, steps: int = 10) -> int:
    polymer, rules = load_polymer(input_path)
    for _ in range(steps):
        polymer = apply_step(polymer, rules)
    counter = Counter(polymer)
    return max(counter.values()) - min(counter.values())


def part_2(input_path: str, steps: int = 40) -> int:
    polymer, rules = load_polymer(input_path)
    pair_counter = Counter()
    for c1, c2 in zip(polymer[:-1], polymer[1:]):
        pair_counter[c1 + c2] += 1

    for _ in range(steps):
        temp_counter = Counter()
        for pair in pair_counter:
            temp_counter[pair[0] + getattr(rules, pair)] += pair_counter[pair]
            temp_counter[getattr(rules, pair) + pair[1]] += pair_counter[pair]
        pair_counter = temp_counter
    char_counter = Counter()
    for pair in pair_counter:
        char_counter[pair[0]] += pair_counter[pair]
    char_counter[polymer[-1]] += 1
    return max(char_counter.values()) - min(char_counter.values())


if __name__ == "__main__":
    import timeit

    input_path = get_local_file_abs_path("input.txt")

    print(timeit.timeit("part_1(input_path)", globals=globals(), number=1))
    print(timeit.timeit("part_2(input_path)", globals=globals(), number=1))
    print(part_1(input_path) == part_2(input_path))
    print(part_1(input_path))
    print(part_2(input_path))
