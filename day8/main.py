import os
from typing import Counter, Dict, List, NewType, Optional

SEGMENT_NUMBERS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
SEGMENT_OCCURENCE = {"e": 4, "b": 6, "f": 9}
STANDARD_MAPPING = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


Note = NewType("Note", List[List[str]])
Mapping = NewType("Mapping", Dict[str, str])
Digits = NewType("Digits", List[str])


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_notes(input_path: str) -> List[Note]:
    def get_pat_and_dig(line: str) -> List[List]:
        return list(map(lambda arr: arr.split(), line.rstrip("\n").split("|")))

    with open(input_path, "r") as file:
        return [get_pat_and_dig(line) for line in file.readlines()]


def part_1(input_path: str) -> int:
    def count_in_note(note: Note, digits) -> int:
        selected_segment_numbers = [SEGMENT_NUMBERS[dig] for dig in digits]
        return len(list(nb for nb in map(len, note[1]) if nb in selected_segment_numbers))

    def count_occurences(notes: List[Note], digits: List[int]) -> int:
        return sum(map(lambda note: count_in_note(note, digits), notes))

    notes = load_notes(input_path)
    return count_occurences(notes, [1, 4, 7, 8])


def part_2(input_path: str) -> int:
    def filter_by_len(list_of_str: List[str], nb_char: int) -> List[str]:
        return list(filter(lambda dig: len(dig) == nb_char, list_of_str))

    def get_segments(note: Note, digit: int) -> str:
        return filter_by_len(note[0], SEGMENT_NUMBERS[digit])[0]

    def find_a(note: Note, mapping: Mapping) -> None:
        one = get_segments(note, 1)
        seven = get_segments(note, 7)
        mapping["a"] = (set(seven) - set(one)).pop()

    def find_c(note: Note, mapping: Mapping) -> None:
        assert mapping["f"]
        one = get_segments(note, 1)
        mapping["c"] = one.replace(mapping["f"], "")

    def find_by_constraint(
        note: Note, mapping: Mapping, seg_target: str, dig: int, reqs: str
    ) -> None:
        assert all(mapping[seg] for seg in reqs)
        segs = get_segments(note, dig)
        for seg in reqs:
            segs = segs.replace(mapping[seg], "")
        mapping[seg_target] = segs

    def find_by_occurence(note: Note, mapping: Mapping, char: str) -> None:
        segment_count = Counter("".join(note[0]))
        for seg, count in segment_count.items():
            if count == SEGMENT_OCCURENCE[char]:
                mapping[char] = seg

    def translate(note: Note, mapping: Mapping) -> int:
        def translate_digit(dig: str, translation: dict) -> Digits:
            return "".join(dig.translate(translation))

        assert all(mapping[seg] for seg in "abcdefg")
        translation = note[1][0].maketrans("".join(mapping.values()), "".join(mapping.keys()))
        return [translate_digit(dig, translation) for dig in note[1]]

    def digits_to_int(digits: Digits) -> int:
        return int("".join(str(STANDARD_MAPPING.index("".join(sorted(digit)))) for digit in digits))

    def translate_note(note: Note) -> int:
        mapping = {seg: "" for seg in "abcdefg"}
        find_a(note, mapping)
        find_by_occurence(note, mapping, "b")
        find_by_occurence(note, mapping, "e")
        find_by_occurence(note, mapping, "f")
        find_c(note, mapping)
        find_by_constraint(note, mapping, "d", 4, "bcf")
        find_by_constraint(note, mapping, "g", 8, "abcdef")
        digits = translate(note, mapping)
        return digits_to_int(digits)

    notes = load_notes(input_path)
    return sum(translate_note(note) for note in notes)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
