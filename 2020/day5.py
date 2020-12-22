def row_col(seat):
    r = 0
    c = 0
    n = 6
    for s in seat[:7]:
        if s == 'B':
            r += 2**n
        n -= 1

    n = 2
    for s in seat[7:]:
        if s == 'R':
            c += 2**n

        n -= 1
    return r, c


if __name__ == '__main__':
    with open('src/day5.txt') as fp:
        lines = [line.strip() for line in fp.readlines()]
        max_seat_id = 0
        max_row = 0
        min_row = 127
        plane = {}
        for line in lines:
            row, col = row_col(line)
            seat_id = row * 8 + col
            if row not in plane:
                plane[row] = [0, 1, 2, 3, 4, 5, 6, 7]
            plane[row].remove(col)
            max_seat_id = max(max_seat_id, seat_id)
            min_row = min(min_row, row)
            max_row = max(max_row, row)

        print(max_seat_id)

        for k, v in plane.items():
            if len(v) > 0 and k not in (min_row, max_row):
                print(k * 8 + v[0])

