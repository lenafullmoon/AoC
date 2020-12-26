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


if __name__ == '__main__':
    with open('src/day24.txt') as fp:
        inputs_ = fp.read()

    black = set()
    for row in inputs_.splitlines():
        do_row(row, black)
    print(len(black))
