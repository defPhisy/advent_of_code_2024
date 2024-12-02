FILE = "./reports.txt"


def main() -> None:
    """Process a report file and count the number of valid reports."""
    # get all lines as list
    lines = get_lines(FILE)

    # map each line to list of integers
    reports = [list(map(int, line.split())) for line in lines]

    # count all reports that are valid
    safe_reports = sum([1 for report in reports if is_valid(report)])
    print(safe_reports)


def get_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def is_valid(report: list[int]) -> bool:
    """
    Determines whether a report is valid. A report is valid if it is either
    strictly increasing or strictly decreasing
    and satisfies the correct distance condition.
    """

    return (is_increasing(report) or is_decreasing(report)) and has_correct_distance(
        report
    )


def is_increasing(report: list[int]) -> bool:
    """Checks if a report is strictly increasing."""

    prev_lvl = report[0]
    for lvl in report[1:]:
        if lvl < prev_lvl:
            return False
        prev_lvl = lvl
    return True


def is_decreasing(report: list[int]) -> bool:
    """Checks if a report is strictly decreasing."""
    prev_lvl = report[0]
    for lvl in report[1:]:
        if lvl > prev_lvl:
            return False
        prev_lvl = lvl
    return True


def has_correct_distance(report: list[int]) -> bool:
    """
    Checks if the distances between consecutive levels in a report
    are within the valid range. The valid range for the distance between
    consecutive levels is 1 to 3 (inclusive).
    """
    prev_lvl = report[0]
    for lvl in report[1:]:
        if abs(lvl - prev_lvl) > 3 or abs(lvl - prev_lvl) < 1:
            return False
        prev_lvl = lvl
    return True


if __name__ == "__main__":
    main()
