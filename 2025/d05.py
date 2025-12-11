def merge_ranges(lower_range, higher_range):
    if lower_range[1] + 1 < higher_range[0]:
        return [lower_range, higher_range]
    if lower_range[0] <= higher_range[0] <= lower_range[1] + 1:
        return [(lower_range[0], max(lower_range[1], higher_range[1]))]


if __name__ == '__main__':
    with open('inputs/d05.txt') as fp:
        inputs_ = fp.read()
    ranges = []
    fresh_count = 0
    range_input = True
    for row in inputs_.splitlines(keepends=False):
        if row == '':
            range_input = False
        elif range_input:
            start, end = row.split('-')
            ranges.append((int(start), int(end)))
        else:
            for r in ranges:
                if r[0] <= int(row) <= r[1]:
                    fresh_count += 1
                    break
    print(fresh_count)

    ranges.sort(key=lambda x: x[0])
    merged_ranges = [ranges.pop(0)]
    while ranges:
        merged_ranges.extend(merge_ranges(merged_ranges.pop(), ranges.pop(0)))

    total = 0
    for r in merged_ranges:
        total += r[1] - r[0] + 1
    print(total)




