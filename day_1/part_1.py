FILE = "./numbers.txt"


def main():
    lines = get_lines(FILE)
    # Split into left and right list
    left_numbers, right_numbers = split_lists(lines)

    # Calculate distance
    distance = 0

    sorted_nums = zip(sorted(left_numbers), sorted(right_numbers))
    distance = sum(map(add_nums, sorted_nums))

    print(distance)


def get_lines(file):
    with open(file, "r") as file:
        lines = file.readlines()
    return lines


def split_lists(lines):
    left_numbers = []
    right_numbers = []

    for line in lines:
        num_1, num_2 = line.split()
        left_numbers.append(num_1)
        right_numbers.append(num_2)
    return left_numbers, right_numbers
    # CORRECT RESULT = 1530215


def add_nums(nums):
    num_1, num_2 = nums
    return abs(int(num_1) - int(num_2))


if __name__ == "__main__":
    main()
