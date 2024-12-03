import re

FILE_PATH = "./memory.txt"

MUL_PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"
DO_PATTERN = r"do\(\)"
DONT_PATTERN = r"don't\(\)"


def get_text(file_path: str) -> str:
    """Reads the content of the specified file and returns it as a string."""

    with open(file_path, "r") as file:
        text = file.read()
    return text


def calculate_sum(muls: list[tuple[str, str]]) -> int:
    """Calculates the sum of the products of pairs of numbers."""

    total = 0
    for num_pair in muls:
        num_1, num_2 = num_pair
        multiplication = int(num_1) * int(num_2)
        total += multiplication
    return total


def get_do_range(
    memory_txt: str, do_ends: list[int], dont_ends: list[int]
) -> list[tuple[int, int]]:
    """Determines the ranges of text between 'do()' and 'don't()' blocks."""

    do_range = []
    start = 0
    end = 0

    for i in range(len(do_ends)):
        end = get_end_index(dont_ends, start)

        if not end:
            start = get_start_index(do_ends, do_range[-1][1])
            end = len(memory_txt) - 1
            do_range.append((start, end))
            break

        do_range.append((start, end))
        start = get_start_index(do_ends, end)

        if not start:
            break

    return do_range


def get_end_index(do_ends: list[int], start: int) -> int | None:
    """Finds the next end index after a given start index."""

    for do in do_ends:
        if do > start:
            return do
    return None


def get_start_index(dont_ends: list[int], end: int) -> int | None:
    """Finds the next start index after a given end index."""

    for dont in dont_ends:
        if dont > end:
            return dont
    return None


def calculate_in_range_of(
    memory_txt: str, do_ranges: list[tuple[int, int]], pattern: str
) -> int:
    """
    Calculates the total sum of all matches of a given pattern
    within specified ranges.
    """

    total = 0
    for start, end in do_ranges:
        mul_numbers = re.findall(pattern, memory_txt[start:end])

        total += calculate_sum(mul_numbers)

    return total
