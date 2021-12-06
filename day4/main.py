from io import FileIO
import os
from typing import List, NewType, Optional, Tuple


GRID_SIZE = 5
CHECKED_VAL = -1

Board = NewType("Board", List[list])


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_board(file: FileIO) -> Board:
    return [
        list(map(int, file.readline().strip("\n").split())) for _ in range(GRID_SIZE)
    ]


def load_bingo(input_path: str) -> Tuple[list[int], List[Board]]:
    boards = []
    with open(input_path, "r") as file:
        drawn_numbers = map(int, file.readline().strip("\n").split(","))
        while file.readline():
            boards.append(load_board(file))

    return (list(drawn_numbers), boards)


def check_col_in_board(board: Board, col_nb: int) -> bool:
    return all(map(lambda line: line[col_nb] == CHECKED_VAL, board))


def find_in_board(
    board: Board, number: int, replacement_number: int = CHECKED_VAL
) -> Optional[int]:
    bingo = False
    total = 0
    for line in board:
        try:
            index = line.index(number)
            line[index] = replacement_number
            bingo = sum(line) == -5 or check_col_in_board(board, index)
        except ValueError:
            pass
        total += sum(filter(lambda val: val != CHECKED_VAL, line))
    return number * total if bingo else None


def find_in_boards(boards: List[Board], number: int) -> Optional[int]:
    for board in boards:
        if score := find_in_board(board, number):
            return score
    return None


def part_1(input_path: str) -> int:
    drawn_numbers, boards = load_bingo(input_path)
    for number in drawn_numbers:
        if (score := find_in_boards(boards, number)) is not None:
            return score


def part_2(input_path: str) -> int:
    with open(input_path, "r") as file:
        pass
    return


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
