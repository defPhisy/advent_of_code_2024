from part_1 import get_lines, is_valid, FILE


def main() -> None:
    """
    Main function to process a report file and count the number
    of safe reports.
    """

    lines = get_lines(FILE)
    reports = [list(map(int, line.split())) for line in lines]

    safe_reports = 0
    for report in reports:
        # check validation from part one
        if is_valid(report):
            safe_reports += 1
            continue
        else:
            # recheck all failed reports for new criteria from part two
            if report_can_remove_one(report):
                safe_reports += 1

    print(safe_reports)


def report_can_remove_one(report: list[int]) -> bool:
    """
    Determines whether a report can become valid by removing exactly one element.
    A report can become valid if the resulting list, after removing one element,
    still satisfies the validity criteria.
    """

    for i in range(len(report)):
        data = report[:i] + report[i + 1 :]
        if is_valid(data):
            return True
    return False


if __name__ == "__main__":
    main()
