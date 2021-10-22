# inputs_ = '389125467'  # 3: 32546789 10: 92658374 # 100 67384529
inputs_ = '469217538'


def decrease_value(value, min_v, max_v):
    return value - 1 if value > min_v else max_v


def cyndex(index, lenc):
    return index % lenc


def mini_cups(rng=100):
    """ No real optimization required"""
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    for _ in range(rng):
        current = circle[current_index]

        out = []
        for i in range(3):
            out.append(
                circle.pop(cyndex(circle.index(current) + 1, len(circle)))
            )

        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)

        insert_index = circle.index(destination)

        for o in out:
            insert_index = cyndex(insert_index + 1, len(circle))
            circle.insert(insert_index, o)

        current_index = circle.index(current)
        current_index = cyndex(current_index + 1, lenc)

    one_index = circle.index(1)
    res = [
        circle[cyndex(one_index + i + 1, lenc)] for i in range(len(circle) - 1)
    ]
    return ''.join(str(x) for x in res)


def min_c_distannce(index1, index2, lenc):
    pos_dst = cyndex(index2 - index1, lenc)
    neg_dst = cyndex(index1 - index2, lenc)
    if pos_dst <= neg_dst:
        return pos_dst
    return -neg_dst


def slide(circle, first_empty, delta, insert, fill):
    lenc = len(circle)
    insert = cyndex(insert - delta + 1, lenc)
    dst = min_c_distannce(first_empty, insert, lenc)
    if dst >= 0:
        from_fill = False
        for i in range(lenc):
            index = cyndex(first_empty + i, lenc)
            if index == insert:
                from_fill = True
            if not from_fill:
                circle[index] = circle[cyndex(index + delta, lenc)]
            else:
                circle[index] = fill[0]
                circle[cyndex(index + 1, lenc)] = fill[1]
                circle[cyndex(index + 2, lenc)] = fill[2]
                break
    else:
        from_fill = False
        for i in range(lenc):
            index = cyndex(first_empty + delta - 1 - i, lenc)
            if index == cyndex(insert + delta, lenc):
                from_fill = True
            if not from_fill:
                circle[index] = circle[cyndex(index - delta, lenc)]
            else:
                circle[index] = fill[0]
                circle[cyndex(index + 1, lenc)] = fill[1]
                circle[cyndex(index + 2, lenc)] = fill[2]
                break


def maxi_cups_slide(length=1000000, rng=10000000):
    """
    Do not do pop and insert, but slide whole sections

    T=42.205 (10000 iterations)
    """
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, length + 1)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    for _ in range(rng):
        current = circle[current_index]

        out = [circle[cyndex(current_index + i + 1, lenc)]
               for i in range(3)]

        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)

        insert_index = circle.index(destination)

        slide(circle, cyndex(current_index + 1, lenc), 3, insert_index, out)

        current_index = circle.index(current)
        current_index = cyndex(current_index + 1, lenc)

    one_at = circle.index(1)
    return circle[cyndex(one_at + 1, lenc)] * circle[cyndex(one_at + 2, lenc)]


def maxi_cups(length=1000000, rng=10000000):
    """
    Mini without helper functions.
    Added insert_index optimization

    T=32.057 (10000 iterations)
    """
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, length + 1)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    insert_index = 0
    for _ in range(rng):
        current = circle[current_index]

        out = [circle[(current_index + 1 + i) % lenc] for i in range(3)]

        for _ in out:
            circle.pop((current_index + 1) % lenc)

        destination = current - 1 if current > min_cup else max_cup
        while destination in out:
            destination = current - 1 if current > min_cup else max_cup

        if destination != circle[insert_index]:
            insert_index = circle.index(destination)

        for o in out:
            insert_index = (insert_index + 1) % len(circle)
            circle.insert(insert_index, o)

        current_index = (circle.index(current) + 1) % lenc

    one_at = circle.index(1)
    return circle[cyndex(one_at + 1, lenc)] * circle[cyndex(one_at + 2, lenc)]


def maxi_cups_deque(length=1000000, rng=10000000):
    """
    Using deque to optimize insertion/deletion.
    Reduce inner functions.
    Added insert_index finding optimization.

    T=18.973 (for 10000 iterations)
    """
    from collections import deque

    circle = deque(int(c) for c in inputs_)
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, length + 1)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    insert_index = 0
    for _ in range(rng):
        current = circle[current_index]

        out = [circle[(current_index + 1 + i) % lenc] for i in range(3)]
        for o in out:
            circle.remove(o)

        destination = current - 1 if current > min_cup else max_cup
        while destination in out:
            destination = current - 1 if current > min_cup else max_cup

        if destination != circle[insert_index]:
            insert_index = circle.index(destination)

        for o in out:
            insert_index = (insert_index + 1) % len(circle)
            circle.insert(insert_index, o)

        current_index = (circle.index(current) + 1) % lenc

    one_at = circle.index(1)
    return circle[cyndex(one_at + 1, lenc)] * circle[cyndex(one_at + 2, lenc)]


def go_linked(circle, indexes, start, steps):
    index = indexes[start]
    nexts = [index]
    for _ in range(steps):
        index = indexes[index]
        nexts.append(index)
    values = [circle[i] for i in nexts[:-1]]
    return values, nexts


def maxi_cups_linked(length=1000000, rng=10000000):
    """
    Use linked list instead of an array.
    Added insert index finding optimization.

    T=0.334 (10000 iterations)
    """
    circle = [int(c) for c in inputs_]
    min_cup = min(circle)
    max_cup = max(circle)
    circle.extend([i for i in range(max_cup + 1, length + 1)])
    max_cup = max(circle)
    lenc = len(circle)
    current_index = 0
    next_index = [
        cyndex(i + 1, lenc) for i in range(lenc)
    ]
    for _ in range(rng):
        current = circle[current_index]

        out, indexes = go_linked(circle, next_index, current_index, 3)

        destination = decrease_value(current, min_cup, max_cup)
        while destination in out:
            destination = decrease_value(destination, min_cup, max_cup)

        if destination == circle[cyndex(destination - 1, len(circle))]:
            insert_index = destination - 1
        else:
            insert_index = circle.index(destination)

        destination_new_next = next_index[current_index]
        end_index_new_next = next_index[insert_index]
        current_index_new_next = indexes[-1]
        next_index[current_index] = current_index_new_next
        next_index[insert_index] = destination_new_next
        next_index[indexes[-2]] = end_index_new_next

        current_index = next_index[current_index]

    one_index = circle.index(1)
    first_after_one_index = next_index[one_index]
    second_after_one_index = next_index[first_after_one_index]
    return circle[first_after_one_index] * circle[second_after_one_index]


if __name__ == '__main__':
    print(mini_cups())

    # print(maxi_cups_deque(rng=10000))
    # print(maxi_cups(rng=10000))
    # print(maxi_cups_slide(rng=10000))
    print(maxi_cups_linked())
