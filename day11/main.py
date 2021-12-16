import os


def neighbours(x: int, y: int) -> set[tuple[int, int]]:
    result = {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}
    result.remove((x, y))
    return result


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_octopuses(input_path: str) -> list[str]:
    with open(input_path, "r") as file:
        return {
            (x, y): int(v)
            for y, line in enumerate(file.readlines())
            for x, v in enumerate(line.strip())
        }


def display_grid(octopuses: dict) -> None:
    height, width = max(x for x, _ in octopuses.keys()) + 1, max(y for _, y in octopuses.keys()) + 1
    for y in range(height):
        print("".join(str(octopuses[x, y]) for x in range(width)))


def pass_a_step(octopuses: dict) -> int:
    def inc_1(pos: tuple[int, int], flashed: set, octopuses: dict) -> None:
        if pos not in flashed and pos in octopuses.keys():
            octopuses[pos] += 1
            if octopuses[pos] > 9:
                flashed.add(pos)
                octopuses[pos] = 0
                for pos_ in neighbours(*pos):
                    inc_1(pos_, flashed, octopuses)
        return flashed, octopuses

    flashed = set()
    for pos in octopuses.keys():
        inc_1(pos, flashed, octopuses)
    return len(flashed)


def part_1(input_path: str, steps: int) -> int:
    octopuses = load_octopuses(input_path)
    flashes_count = 0
    for _ in range(steps):
        flashes_count += pass_a_step(octopuses)
    display_grid(octopuses)
    return flashes_count


def part_2(input_path: str, steps: int) -> int | None:
    octopuses = load_octopuses(input_path)
    for i in range(10000):
        if (pass_a_step(octopuses)) == len(octopuses):
            display_grid(octopuses)
            return i + 1
    display_grid(octopuses)
    return None


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path, 100))
    print(part_2(input_path, 100))
