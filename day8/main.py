import os
from typing import List

SEGMENT_NUMBERS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_notes(input_path: str) -> List[int]:
    def get_pat_and_dig(line: str) -> List[List]:
        return list(map(lambda arr: arr.split(), line.rstrip("\n").split("|")))

    with open(input_path, "r") as file:
        return [get_pat_and_dig(line) for line in file.readlines()]


def count_in_note(note, digits) -> int:
    selected_segment_numbers = [SEGMENT_NUMBERS[dig] for dig in digits]
    return len(list(nb for nb in map(len, note[1]) if nb in selected_segment_numbers))


def count_occurences(notes, digits: List[int]) -> int:
    return sum(map(lambda note: count_in_note(note, digits), notes))


def part_1(input_path: str) -> int:
    notes = load_notes(input_path)
    return count_occurences(notes, [1, 4, 7, 8])


def part_2(input_path: str) -> int:
    notes = load_notes(input_path)
    return count_occurences(notes, [1, 4, 7, 8])


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
