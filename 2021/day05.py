def draw_line(point_a, point_b):
    dotted_line = []
    dir_x = 1 if point_a[0] <= point_b[0] else -1
    dir_y = 1 if point_a[1] <= point_b[1] else -1
    i, j = point_a[0], point_a[1]
    while True:
        dotted_line.append((i, j))
        if i == point_b[0] and j == point_b[1]:
            break
        if i != point_b[0]:
            i += dir_x
        if j != point_b[1]:
            j += dir_y
    return dotted_line


if __name__ == '__main__':
    with open('src/day05.txt') as fp:
        inputs_ = fp.read()

    lines = []
    for line in inputs_.splitlines():
        a, b = line.split(' -> ')
        a = a.split(',')
        b = b.split(',')
        lines.append(((int(a[0]), int(a[1])), (int(b[0]), int(b[1]))))
    dots_1 = {}
    dots_2 = {}
    for line in lines:
        for dot in draw_line(line[0], line[1]):
            if dot not in dots_2:
                dots_2[dot] = 1
            else:
                dots_2[dot] += 1
            if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
                if dot not in dots_1:
                    dots_1[dot] = 1
                else:
                    dots_1[dot] += 1

    print(sum(1 if v > 1 else 0 for v in dots_1.values()))
    print(sum(1 if v > 1 else 0 for v in dots_2.values()))
