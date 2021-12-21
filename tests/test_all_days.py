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
import day11.main
import day12.main
import day13.main
import day14.main
import day15.main
import pytest


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


@pytest.mark.parametrize(
    ("day_module", "args", "expected_1", "expected_2"),
    [
        (
            day02.main,
            [get_local_file_abs_path("day02.txt")],
            150,
            900,
        ),
        (
            day03.main,
            [get_local_file_abs_path("day03.txt")],
            (198, "10110", "01001"),
            (230, "10111", "01010"),
        ),
        (
            day04.main,
            [get_local_file_abs_path("day04.txt")],
            (4512),
            (1924),
        ),
        (
            day05.main,
            [get_local_file_abs_path("day05.txt")],
            (5),
            (12),
        ),
        (
            day06.main,
            [get_local_file_abs_path("day06.txt"), 256],
            (26984457539),
            (26984457539),
        ),
        (
            day07.main,
            [get_local_file_abs_path("day07.txt")],
            (37),
            (168),
        ),
        (
            day08.main,
            [get_local_file_abs_path("day08.txt")],
            (26),
            (61229),
        ),
        (
            day09.main,
            [get_local_file_abs_path("day09.txt")],
            (15),
            (1134),
        ),
        (
            day10.main,
            [get_local_file_abs_path("day10.txt")],
            (26397),
            (288957),
        ),
        (
            day11.main,
            [get_local_file_abs_path("day11.txt"), 100],
            (1656),
            (195),
        ),
        (
            day12.main,
            [get_local_file_abs_path("day12.txt")],
            (10),
            (36),
        ),
        (
            day13.main,
            [get_local_file_abs_path("day13.txt")],
            (17),
            (17),
        ),
        (
            day14.main,
            [get_local_file_abs_path("day14.txt")],
            (1588),
            (2188189693529),
        ),
        (
            day15.main,
            [get_local_file_abs_path("day15.txt")],
            (40),
            (2188189693529),
        ),
    ],
)
class TestDay:
    def test_part_1(self, day_module, args, expected_1, expected_2) -> None:
        assert day_module.part_1(*args) == expected_1

    def test_part_2(self, day_module, args, expected_1, expected_2) -> None:
        assert day_module.part_2(*args) == expected_2
