def p1(inp):
    reports = [list(map(int, line.strip().split(" "))) for line in inp]

    safe_reports = 0

    for report in reports:
        all_increasing = all(levels[1] - levels[0] > 0 for levels in zip(report, report[1:]))
        all_decreasing = all(levels[1] - levels[0] < 0 for levels in zip(report, report[1:]))
        all_safe_diff = all(0 <= abs(levels[1] - levels[0]) <= 3 for levels in zip(report, report[1:]))

        if (all_increasing or  all_decreasing) and all_safe_diff:
            safe_reports += 1

    return safe_reports


def p2(inp):
    reports = [list(map(int, line.strip().split(" "))) for line in inp]

    safe_reports = 0

    for report in reports:
        for modified_report in [report[:i] + report[i+1:] for i in range(len(report))]:
            all_increasing = all(levels[1] - levels[0] > 0 for levels in zip(modified_report, modified_report[1:]))
            all_decreasing = all(levels[1] - levels[0] < 0 for levels in zip(modified_report, modified_report[1:]))
            all_safe_diff = all(0 <= abs(levels[1] - levels[0]) <= 3 for levels in zip(modified_report, modified_report[1:]))

            if (all_increasing or all_decreasing) and all_safe_diff:
                safe_reports += 1
                break


    return safe_reports


with open('./input/week1/day2.txt') as file:
    lines = file.readlines()

    print('part 1: {}'.format(p1(lines)))
    print('part 2: {}'.format(p2(lines)))
