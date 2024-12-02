from part_1 import get_lines, is_valid, FILE


def main():
    lines = get_lines(FILE)
    reports = [list(map(int, line.split())) for line in lines]

    safe_reports = 0
    for report in reports:
        if is_valid(report):
            safe_reports += 1
            continue
        else:
            if report_can_remove_one(report):
                safe_reports += 1

    print(safe_reports)


def report_can_remove_one(report):
    for i in range(len(report)):
        data = report[:i] + report[i + 1 :]
        if is_valid(data):
            return True
    return False


if __name__ == "__main__":
    main()
