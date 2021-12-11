def draw_line(point_a, point_b):
    dotted_line = []
    dir_x = 1 if point_a[0] <= point_b[0] else -1
    dir_y = 1 if point_a[1] <= point_b[1] else -1
    i, j = point_a[0], point_a[1]
    while True:
        dotted_line.append((i, j))
        if i == point_b[0] and j == point_b[1]:
            return dotted_line
        i += dir_x if i != point_b[0] else 0
        j += dir_y if j != point_b[1] else 0


if __name__ == '__main__':
    with open('src/day05.txt') as fp:
        inputs_ = fp.read()

    freq_1 = {}
    freq_2 = {}
    for row in inputs_.splitlines():
        a0, a1, b0, b1 = row.replace(' -> ', ',').split(',')
        a0, a1, b0, b1 = int(a0), int(a1), int(b0), int(b1)
        for dot in draw_line((a0, a1), (b0, b1)):
            freq_2[dot] = freq_2[dot] + 1 if dot in freq_2 else 1
            if a0 == b0 or a1 == b1:
                freq_1[dot] = freq_1[dot] + 1 if dot in freq_1 else 1

    print(sum(1 for v in freq_1.values() if v > 1))
    print(sum(1 for v in freq_2.values() if v > 1))
