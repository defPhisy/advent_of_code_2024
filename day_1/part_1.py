FILE = "./numbers.txt"


def main() -> None:
    """Calculate the sum of distances between pairs of numbers."""

    lines = get_lines(FILE)

    # Split into left and right list
    left_numbers, right_numbers = split_lists(lines)

    # Combine sorted lists
    sorted_nums = zip(sorted(left_numbers), sorted(right_numbers))

    # Calculate distance
    distance = sum(map(add_nums, sorted_nums))

    # CORRECT RESULT = 1530215
    print(distance)


def get_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def split_lists(lines: list[str]) -> tuple[list[str], list[str]]:
    """Splits lines of number pairs into two separate lists."""

    left_numbers = []
    right_numbers = []

    for line in lines:
        num_1, num_2 = line.split()
        left_numbers.append(num_1)
        right_numbers.append(num_2)
    return left_numbers, right_numbers


def add_nums(nums: tuple[str, str]) -> int:
    """Computes the absolute difference between two numbers."""

    num_1, num_2 = nums
    return abs(int(num_1) - int(num_2))


if __name__ == "__main__":
    main()
