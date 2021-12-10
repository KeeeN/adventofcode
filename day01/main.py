import os


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def part_1() -> int:
    with open(get_local_file_abs_path("input.txt"), "r") as file:
        larger_count = 0
        prev = None
        for line in file.readlines():
            if prev and int(line) > prev:
                larger_count += 1
            prev = int(line)
    return larger_count


def part_2() -> int:
    with open(get_local_file_abs_path("input.txt"), "r") as file:
        larger_count = 0
        prev_sum = None
        lines_a = file.readlines()
        lines_b = lines_a[1:]
        lines_c = lines_a[2:]
        for window in zip(lines_a, lines_b, lines_c):
            window_sum = sum(map(int, window))
            if prev_sum and window_sum > prev_sum:
                larger_count += 1
            prev_sum = window_sum
    return larger_count


if __name__ == "__main__":
    print(part_1())
    print(part_2())
