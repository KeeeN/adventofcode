import os
from enum import Enum

import numpy as np


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_sheet(input_path: str) -> tuple[np.ndarray, list[list[str]]]:
    sheet = np.zeros((1, 1), dtype=int)
    with open(input_path, "r") as file:
        height = 0
        width = 0
        lines = file.readlines()
        points = []
        folds = []
        for line in lines:
            if stripped := line.strip():
                if stripped.startswith("fold"):
                    axis, value = stripped.strip("fold along ").split("=")
                    folds.append((axis, int(value)))
                else:
                    x, y = map(int, stripped.split(","))
                    width = max(width, x + 1)
                    height = max(height, y + 1)
                    points.append((x, y))
        sheet.resize((height, width))
        for point in points:
            sheet[point[1], point[0]] = 1
    return sheet, folds


class Axis(str, Enum):
    X = "x"
    Y = "y"


def fold_sheet(sheet: np.ndarray, fold: int, axis: Axis) -> np.ndarray:
    match axis:
        case Axis.X:
            left = sheet[:, :fold]
            right = sheet[:, fold + 1 :]
            folded = left | right[:, ::-1]
        case Axis.Y:
            top = sheet[:fold, :]
            bottom = sheet[fold + 1 :, :]
            folded = top | bottom[::-1, :]
    return folded


def part_1(input_path: str) -> int:
    sheet, folds = load_sheet(input_path)
    folded = fold_sheet(sheet=sheet, axis=folds[0][0], fold=folds[0][1])
    return (folded == 1).sum()


def part_2(input_path: str) -> int:
    sheet, folds = load_sheet(input_path)
    for fold in folds:
        sheet = fold_sheet(sheet=sheet, axis=fold[0], fold=fold[1])
    for line in sheet:
        print("".join(map(lambda e: " " if e == 0 else "X", line)))
    return 17


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
