from ..main import part_1, part_2
import os


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def test_part_1() -> None:
    input_path = get_local_file_abs_path("test_input.txt")
    assert part_1(input_path) == (198, "10110", "01001")


def test_part_2() -> None:
    input_path = get_local_file_abs_path("test_input.txt")
    assert part_2(input_path) == (230, "10111", "01010")