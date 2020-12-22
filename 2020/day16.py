def parse_inputs_header(lines):
    valid_ranges = {}
    for line in lines[:lines.index('your ticket:') - 1]:
        name, ranges = line.split(': ')
        range_1, range_2 = ranges.split(' or ')
        range_1 = range_1.split('-')
        range_2 = range_2.split('-')
        valid_ranges[name] = set()
        for n in range(int(range_1[0]), int(range_1[1]) + 1):
            valid_ranges[name].add(n)
        for n in range(int(range_2[0]), int(range_2[1]) + 1):
            valid_ranges[name].add(n)
    my_ticket = [int(n)
                 for n in lines[lines.index('your ticket:') + 1].split(',')]
    return valid_ranges, my_ticket


def scanning_errors(lines):
    valid_ranges, _ = parse_inputs_header(lines)
    valid_set = {n for vr in valid_ranges.values() for n in vr}
    error_sum = 0
    for line in lines[lines.index('nearby tickets:') + 1:]:
        for tn in [int(n) for n in line.split(',')]:
            if tn not in valid_set:
                error_sum += tn
    return error_sum


def deduce(lines):
    valid_ranges, my_ticket = parse_inputs_header(lines)
    valid_set = {n for vr in valid_ranges.values() for n in vr}

    possible_fields = [set(valid_ranges) for _ in range(len(my_ticket))]
    for line in lines[lines.index('nearby tickets:') + 1:]:
        nums = [int(n) for n in line.split(',')]
        if any(n not in valid_set for n in nums):
            continue
        for i, n in enumerate(nums):
            keep = {f for f in possible_fields[i] if n in valid_ranges[f]}
            possible_fields[i] = possible_fields[i].intersection(keep)

    field_to_index = {}
    while len(field_to_index) < len(my_ticket):
        for i, pfs in enumerate(possible_fields):
            if len(pfs) == 1:
                field_to_index[pfs.pop()] = i
                break
        possible_fields = [pf.difference(set(field_to_index))
                           for pf in possible_fields]

    mul = 1
    for field, index in field_to_index.items():
        mul *= my_ticket[index] if field.startswith('departure') else 1
    return mul


if __name__ == '__main__':
    with open('src/day16.txt') as fp:
        inputs = fp.read()
    print(scanning_errors(inputs.splitlines()))
    print(deduce(inputs.splitlines()))
