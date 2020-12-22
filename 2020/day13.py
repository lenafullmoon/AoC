from collections import OrderedDict


def find_bus(lines):
    depart_after = int(lines[0])
    buses = [int(b) for b in lines[1].split(',') if b != 'x']
    earliest, wait = 0, depart_after
    for b in buses:
        around = (depart_after // b) * b
        if around < depart_after:
            around += b

        if wait > around - depart_after:
            wait = around - depart_after
            earliest = b
    print(earliest * wait)


def works_but_slow(lines):
    schedule = [int(b) if b != 'x' else 0 for b in lines[1].split(',')]
    rarest_bus = max(schedule)
    schedule_copy = schedule.copy()
    schedule_copy.remove(rarest_bus)
    s_rarest_bus = max(schedule_copy)
    rarest_index = schedule.index(rarest_bus)
    s_rarest_diff = schedule.index(s_rarest_bus) - rarest_index
    t = rarest_bus
    while True:
        t += rarest_bus
        if (t + s_rarest_diff) % s_rarest_bus != 0:
            continue
        found = False
        for i in range(0, len(schedule)):
            if schedule[i] == 0:
                continue
            dep_time = t + (i - rarest_index)
            if dep_time % schedule[i] != 0:
                break
        else:
            found = True
        if found:
            break
    return t - rarest_index


def restruct(lines):
    schedule = OrderedDict()
    buses = [int(b) if b != 'x' else 0 for b in lines[1].split(',')]
    bus_index = [bi for bi in zip(buses, range(len(buses))) if bi[0] != 0]
    bus_index.sort(reverse=True)
    for bus, index in bus_index:
        schedule[bus] = index
    rarest_bus = max(schedule)
    rarest_index = schedule[rarest_bus]
    t = 0
    inc = rarest_bus
    last_found_place = 0
    while True:
        t += inc
        found = False
        place = -1
        for bus, index in schedule.items():
            place += 1
            dep_time = t + (index - rarest_index)
            if dep_time % bus != 0:
                break
            elif place > last_found_place:
                last_found_place = place
                inc *= bus
        else:
            found = True
        if found:
            break
    return t - rarest_index


if __name__ == '__main__':
    with open('src/day13.txt') as fp:
        lines = fp.read()
    lines = lines.splitlines()
    find_bus(lines)

    # print(works_but_slow(lines))
    print(restruct(lines))
