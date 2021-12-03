import os

import day3.main
import day2.main
import pytest


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


@pytest.mark.parametrize(
    ("day_module", "args", "expected_1", "expected_2"),
    [
        (
            day2.main,
            [get_local_file_abs_path("day2_test_input.txt")],
            150,
            900,
        ),
        (
            day3.main,
            [get_local_file_abs_path("day3_test_input.txt")],
            (198, "10110", "01001"),
            (230, "10111", "01010"),
        )
    ],
)
class TestDay:
    def test_part_1(self, day_module, args, expected_1, expected_2) -> None:
        assert day_module.part_1(*args) == expected_1

    def test_part_2(self, day_module, args, expected_1, expected_2) -> None:
        assert day_module.part_2(*args) == expected_2
