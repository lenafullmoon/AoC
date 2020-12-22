inputs_ = '''..#..#..
#.#...#.
..#.....
##....##
#..#.###
.#..#...
###..#..
....#..#'''


def get_near(x, y, z, w=None):
    eps = (-1, 2)
    if w is None:
        coords = [(x + i, y + j, z + k)
                  for i in range(*eps) for j in range(*eps)
                  for k in range(*eps)]
        coords.remove((x, y, z))
    else:
        coords = [(x + i, y + j, z + k, w + m)
                  for i in range(*eps) for j in range(*eps)
                  for k in range(*eps) for m in range(*eps)]
        coords.remove((x, y, z, w))
    return coords


def calculate(coord, active_map):
    near_active = sum(1 for coord in get_near(*coord)
                      if coord in active_map and active_map[coord])
    return near_active == 3 or (near_active == 2
                                and active_map.get(coord, False))


def space_3d(inputs):
    active_map = {(i, j, 0): inputs[i][j] == '#'
                  for i in range(len(inputs)) for j in range(len(inputs[0]))}

    range_x = range(0, len(inputs))
    range_y = range(0, len(inputs[0]))
    range_z = range(0, 1)
    for _ in range(6):
        range_x = range(range_x.start - 1, range_x.stop + 1)
        range_y = range(range_y.start - 1, range_y.stop + 1)
        range_z = range(range_z.start - 1, range_z.stop + 1)
        active_map = {(i, j, k): calculate((i, j, k), active_map)
                      for i in range_x for j in range_y for k in range_z}
    print(sum(1 for x in active_map.values() if x))


def space_4d(inputs):
    start = {}
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            start[(i, j, 0, 0)] = inputs[i][j] == '#'
    range_x = range(0, len(inputs))
    range_y = range(0, len(inputs[0]))
    range_z = range(0, 1)
    range_w = range(0, 1)
    old = start
    for _ in range(6):
        range_x = range(range_x.start - 1, range_x.stop + 1)  # TODO contain
        range_y = range(range_y.start - 1, range_y.stop + 1)
        range_z = range(range_z.start - 1, range_z.stop + 1)
        range_w = range(range_w.start - 1, range_w.stop + 1)
        new = {}
        for i in range_x:
            for j in range_y:
                for k in range_z:
                    for m in range_w:
                        coord = (i, j, k, m)
                        new[coord] = calculate(coord, old)
        old = new.copy()
    print(sum(1 if x else 0 for x in old.values()))


if __name__ == '__main__':
    space_3d(inputs_.splitlines())
    space_4d(inputs_.splitlines())
