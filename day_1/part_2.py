from part_1 import get_lines, split_lists, FILE


def main():
    lines = get_lines(FILE)
    left_numbers, right_numbers = split_lists(lines)

    # map string numbers to integers
    left_numbers = list(map(int, left_numbers))
    right_numbers = list(map(int, right_numbers))

    # calculate similarity of lists
    total_similarity = 0
    for num in left_numbers:
        multiplicand = right_numbers.count(num)
        similarity = num * multiplicand
        total_similarity += similarity

    print(total_similarity)
    # CORRECT RESULT = 26800609


if __name__ == "__main__":
    main()
