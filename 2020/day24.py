# e, se, sw, w, nw, and ne
#    ne  nw         ^   +y     +x
#  e   O   w       | |
#    se  sw         v      +z


def do_row(row, black):
    last = None
    current = (0, 0, 0)
    new = current
    for c in row:
        if not last and (c == 'w' or c == 'e'):
            if c == 'w':
                new = current[0] - 1, current[1] + 1, current[2]
            elif c == 'e':
                new = current[0] + 1, current[1] - 1, current[2]
        elif last and (c == 'w' or c == 'e'):
            if last == 'n' and c == 'w':
                new = current[0], current[1] + 1, current[2] - 1
            elif last == 'n' and c == 'e':
                new = current[0] + 1, current[1], current[2] - 1
            elif last == 's' and c == 'w':
                new = current[0] - 1, current[1], current[2] + 1
            elif last == 's' and c == 'e':
                new = current[0], current[1] - 1, current[2] + 1
            last = None
        else:
            last = c
            continue
        current = new
    if new in black:
        black.remove(new)
    else:
        black.add(new)


def find_near(current):
    return {
        (current[0] - 1, current[1] + 1, current[2]),
        (current[0] + 1, current[1] - 1, current[2]),
        (current[0], current[1] + 1, current[2] - 1),
        (current[0] + 1, current[1], current[2] - 1),
        (current[0] - 1, current[1], current[2] + 1),
        (current[0], current[1] - 1, current[2] + 1)
    }


def daily_toggle(black):
    white_tiles = set()
    to_white = set()
    to_black = set()
    for tile in black:
        near = find_near(tile)
        white_tiles = white_tiles.union(near - black)
        black_near_cnt = len(near & black)
        if black_near_cnt == 0 or black_near_cnt > 2:
            to_white.add(tile)
    for tile in white_tiles:
        near = find_near(tile)
        black_near_cnt = len(near & black)

        if black_near_cnt == 2:
            to_black.add(tile)
    black = black.union(to_black)
    black = black - to_white
    return black


if __name__ == '__main__':
    with open('src/day24.txt') as fp:
        inputs_ = fp.read()

    black_tiles = set()
    for row in inputs_.splitlines():
        do_row(row, black_tiles)
    print(len(black_tiles))

    for _ in range(100):
        black_tiles = daily_toggle(black_tiles)
    print(len(black_tiles))
