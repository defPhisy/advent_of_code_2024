FILE = "./reports.txt"


def main():
    lines = get_lines(FILE)
    reports = [list(map(int, line.split())) for line in lines]

    safe_reports = 0
    for current_lvl in reports:
        if is_valid(current_lvl):
            safe_reports += 1

    print(safe_reports)


def get_lines(file):
    with open(file, "r") as file:
        lines = file.readlines()
    return lines


def is_valid(current_lvl):
    return (
        is_increasing(current_lvl) or is_decreasing(current_lvl)
    ) and has_correct_distance(current_lvl)


def is_increasing(report):
    prev_lvl = report[0]
    for lvl in report[1:]:
        if lvl < prev_lvl:
            return False
        prev_lvl = lvl
    return True


def is_decreasing(report):
    prev_lvl = report[0]
    for lvl in report[1:]:
        if lvl > prev_lvl:
            return False
        prev_lvl = lvl
    return True


def has_correct_distance(report):
    prev_lvl = report[0]
    for lvl in report[1:]:
        if abs(lvl - prev_lvl) > 3 or abs(lvl - prev_lvl) < 1:
            return False
        prev_lvl = lvl
    return True


if __name__ == "__main__":
    main()
