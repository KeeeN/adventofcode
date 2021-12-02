import os


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def main() -> int:
    with open(get_local_file_abs_path("input.txt"), "r") as file:
        larger_count = 0
        prev = None
        for line in file.readlines():
            if prev and int(line) > prev:
                larger_count += 1
            prev = int(line)
    return larger_count


if __name__ == "__main__":
    print(main())
