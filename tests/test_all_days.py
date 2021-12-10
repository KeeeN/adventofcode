import os

import day02.main
import day03.main
import day04.main
import day05.main
import day06.main
import day07.main
import day08.main
import day09.main
import day10.main
import pytest


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


@pytest.mark.parametrize(
    ("day_module", "args", "expected_1", "expected_2"),
    [
        (
            day02.main,
            [get_local_file_abs_path("day02_test_input.txt")],
            150,
            900,
        ),
        (
            day03.main,
            [get_local_file_abs_path("day03_test_input.txt")],
            (198, "10110", "01001"),
            (230, "10111", "01010"),
        ),
        (
            day04.main,
            [get_local_file_abs_path("day04_test_input.txt")],
            (4512),
            (1924),
        ),
        (
            day05.main,
            [get_local_file_abs_path("day05_test_input.txt")],
            (5),
            (12),
        ),
        (
            day06.main,
            [get_local_file_abs_path("day06_test_input.txt"), 256],
            (26984457539),
            (26984457539),
        ),
        (
            day07.main,
            [get_local_file_abs_path("day07_test_input.txt")],
            (37),
            (168),
        ),
        (
            day08.main,
            [get_local_file_abs_path("day08_test_input.txt")],
            (26),
            (61229),
        ),
        (
            day09.main,
            [get_local_file_abs_path("day09_test_input.txt")],
            (15),
            (1134),
        ),
        (
            day10.main,
            [get_local_file_abs_path("day10_test_input.txt")],
            (26397),
            (288957),
        ),
    ],
)
class TestDay:
    def test_part_1(self, day_module, args, expected_1, expected_2) -> None:
        assert day_module.part_1(*args) == expected_1

    def test_part_2(self, day_module, args, expected_1, expected_2) -> None:
        assert day_module.part_2(*args) == expected_2
