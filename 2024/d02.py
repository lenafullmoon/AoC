def is_report_safe(report):
    diffs = [b - a for a, b in zip(report[:-1], report[1:])]
    return all(abs(d) <= 3 for d in diffs) and (
            all(d < 0 for d in diffs) or all(d > 0 for d in diffs)
    )


if __name__ == '__main__':
    with open('inputs/d02.txt') as fp:
        inputs_ = fp.read()

    reports = [[int(x.strip()) for x in row.split()]
               for row in inputs_.splitlines(keepends=False)]

    count_safe = 0
    count_damp_safe = 0
    for report in reports:
        if is_report_safe(report):
            count_safe += 1
        else:
            for i in range(len(report)):
                damp_report = report.copy()
                damp_report.pop(i)
                if is_report_safe(damp_report):
                    count_damp_safe += 1
                    break

    print(count_safe)
    print(count_safe + count_damp_safe)
