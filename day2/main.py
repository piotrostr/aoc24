import os

MAX_SAFE_DIFF = 3


def is_safe(
    report: list[int],
) -> bool:
    inc_diffs = [
        0 < report[i + 1] - report[i] <= MAX_SAFE_DIFF for i in range(len(report) - 1)
    ]

    dec_diffs = [
        0 < report[i] - report[i + 1] <= MAX_SAFE_DIFF for i in range(len(report) - 1)
    ]

    inc_ok = all(inc_diffs)
    dec_ok = all(dec_diffs)
    if inc_ok or dec_ok:
        return True
    return False


def can_be_made_safe(report: list[int]) -> bool:
    if len(report) <= 1:
        return True

    # First check if it's already safe
    if is_safe(report):
        return True

    # Try removing each element one at a time
    for i in range(len(report)):
        # Create new list without element at index i
        new_report = report[:i] + report[i + 1 :]
        if is_safe(new_report):
            return True

    return False


if __name__ == "__main__":
    with open(
        "./example.txt" if os.getenv("TEST") is not None else "./input.txt", "r"
    ) as f:
        lines = f.read().splitlines()

    reports = [[int(i) for i in line.split(" ")] for line in lines]

    safe = 0

    for report in reports:
        if report.__len__() == 1:
            safe += 1
            continue

        if report[0] == report[1]:
            continue

        if is_safe(report):
            safe += 1

    print(safe)

    safe = sum(1 for report in reports if can_be_made_safe(report))

    print(safe)
