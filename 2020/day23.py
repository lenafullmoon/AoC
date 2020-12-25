# inputs_ = '389125467'  # 3: 32546789 10: 92658374 # 100 67384529
inputs_ = '469217538'


def decrease_value(value, min_v, max_v):
    res = value - 1
    if res < min_v:
        res = max_v
    return res


def cyndex(index, lenc):
    return index % lenc


def final(circle):
    one_index = circle.index(1)
    res = []
    for i in range(len(circle) - 1):
        res.append(circle[cyndex(one_index + i + 1, len(circle))])
    return ''.join(str(x) for x in res)


def mini_cups():
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    destination = -1
    for _ in range(100):
        out = []
        current = circle[current_index]
        cp_circle = circle.copy()

        for i in range(3):
            out.append(
                cp_circle.pop(cyndex(cp_circle.index(current) + 1, len(cp_circle)))
            )
        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)
        insert_index = cp_circle.index(destination)
        for o in out:
            insert_index = cyndex(insert_index + 1, len(cp_circle))
            cp_circle.insert(insert_index, o)
        circle = cp_circle
        current_index = circle.index(current)
        current_index = cyndex(current_index + 1, len(circle))

        # print(out, current, destination)
    print(final(circle))


def slide(circle, first_empty, delta, insert, fill):
    lenc = len(circle)
    insert = cyndex(insert - delta + 1, lenc)
    from_fill = False
    for i in range(lenc):
        index = cyndex(first_empty + i, lenc)
        if index == insert:
            from_fill = True
        if not from_fill:
            circle[index] = circle[cyndex(index + delta, lenc)]
        else:
            circle[index] = fill.pop(0)
        if len(fill) == 0:
            break

import utils


@utils.print_duration
def maxi_cups_slide():
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, 1000001)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    destination = -1
    # for xx in range(100):
    for xx in range(100):
        if xx % 100 == 0:
            print(xx)
        out = []
        current = circle[current_index]
        # cp_circle = circle.copy()
        # print(circle)
        for i in range(3):
            out.append(
                circle[cyndex(current_index + i + 1, lenc)]
            )
        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)
        insert_index = circle.index(destination)
        # print(out, current, destination)

        slide(circle, cyndex(current_index + 1, lenc), 3, insert_index, out)

        current_index = cyndex(current_index + 1, lenc)
    # print(final(circle))


@utils.print_duration
def maxi_cups():
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, 1000001)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    destination = -1
    # for xx in range(100):
    for xx in range(10000):
        if xx % 1000 == 0:
            print(xx)
        out = []
        current = circle[current_index]
        cp_circle = circle.copy()
        # print(cp_circle)
        for i in range(3):
            out.append(
                cp_circle.pop((cp_circle.index(current) + 1) % len(cp_circle))
            )
        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)
        insert_index = cp_circle.index(destination)
        for o in out:
            insert_index = (insert_index + 1) % len(cp_circle)
            cp_circle.insert(insert_index, o)
        circle = cp_circle
        current_index = circle.index(current)
        current_index = (current_index + 1) % lenc

        # print(out, current, destination)
    one_index = circle.index(1)
    res = []
    for i in range(lenc - 1):
        res.append(circle[(one_index + i + 1)% lenc])
        if len(res) == 2:
            break
    print(res[0] * res[1])

@utils.print_duration
def maxi_cups_slicing():
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, 1000001)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    destination = -1
    for xx in range(10000):
    # for xx in range(1000):
        if xx % 1000 == 0:
            print(xx)
        out = []
        current = circle[current_index]
        # cp_circle = circle.copy()
        # print(xx + 1, circle)
        out = [
            circle[(current_index + 1) % lenc],
            circle[(current_index + 2) % lenc],
            circle[(current_index + 3) % lenc]
        ]

        # for i in range(3):
        #     out.append(
        #         cp_circle.pop((cp_circle.index(current) + 1) % len(cp_circle))
        #     )
        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)

        insert_index = (circle.index(destination) + 1) % lenc
        curr_index_1 = (current_index + 1) % lenc
        curr_index_4 = (current_index + 4) % lenc
        if insert_index > curr_index_4 > curr_index_1:
            circle = circle[: curr_index_1] + \
                circle[curr_index_4: insert_index] + out + \
                circle[insert_index:]
        elif curr_index_4 > curr_index_1 > insert_index:
            circle = circle[: insert_index] + out +\
                circle[insert_index: curr_index_1] + \
                circle[curr_index_4 :]
        elif curr_index_1 > insert_index > curr_index_4:
            circle = circle[curr_index_4:insert_index] + out + \
                circle[insert_index:curr_index_1]
        else:
            circle = circle
            print('ERROR', curr_index_1, curr_index_4, insert_index)

        # for o in out:
        #     insert_index = (insert_index + 1) % len(cp_circle)
        #     cp_circle.insert(insert_index, o)
        #     cp_circle.
        # circle = cp_circle
        current_index = circle.index(current)
        current_index = (current_index + 1) % lenc

        # print(out, current, destination)
    # print(final(circle))
    one_index = circle.index(1)
    res = []
    for i in range(lenc - 1):
        res.append(circle[(one_index + i + 1)% lenc])
        if len(res) == 2:
            break
    print(res[0] * res[1])


if __name__ == '__main__':
    mini_cups()
    maxi_cups_slicing()
    # maxi_cups()

# -- move 1 --
# cups: (3) 8  9  1  2  5  4  6  7
# pick up: 8, 9, 1
# destination: 2
#
# -- move 2 --
# cups:  3 (2) 8  9  1  5  4  6  7
# pick up: 8, 9, 1
# destination: 7
#
# -- move 3 --
# cups:  3  2 (5) 4  6  7  8  9  1
# pick up: 4, 6, 7
# destination: 3
#
# -- move 4 --
# cups:  7  2  5 (8) 9  1  3  4  6
# pick up: 9, 1, 3
# destination: 7
#
# -- move 5 --
# cups:  3  2  5  8 (4) 6  7  9  1
# pick up: 6, 7, 9
# destination: 3
#
# -- move 6 --
# cups:  9  2  5  8  4 (1) 3  6  7
# pick up: 3, 6, 7
# destination: 9
#
# -- move 7 --
# cups:  7  2  5  8  4  1 (9) 3  6
# pick up: 3, 6, 7
# destination: 8
#
# -- move 8 --
# cups:  8  3  6  7  4  1  9 (2) 5
# pick up: 5, 8, 3
# destination: 1
#
# -- move 9 --
# cups:  7  4  1  5  8  3  9  2 (6)
# pick up: 7, 4, 1
# destination: 5
#
# -- move 10 --
# cups: (5) 7  4  1  8  3  9  2  6
# pick up: 7, 4, 1
# destination: 3
#
# -- final --
# cups:  5 (8) 3  7  4  1  9  2  6