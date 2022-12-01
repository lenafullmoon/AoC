inputs_ = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
'''
from pprint import pprint
import math


def parse_tiles(lines):
    tiles = {}
    last_tile = 0
    for line in lines:
        if line == '':
            continue
        if line.startswith('Tile'):
            last_tile = int(line[5:-1])
            tiles[last_tile] = []
        else:
            tiles[last_tile].append([c for c in line])
    return tiles


def tiles_in_categories(tiles):
    borders = tiles_to_borders(tiles)
    corners, edges, middle = set(), set(), set()
    possible_conns = {}

    for t_id, b in borders.items():
        possible_conns[t_id] = set()
        for t2_id, b2 in borders.items():
            if t_id == t2_id:
                continue
            for border in b:
                if border in b2:
                    possible_conns[t_id].add(t2_id)
        if len(possible_conns[t_id]) == 2:
            corners.add(t_id)
        elif len(possible_conns[t_id]) == 3:
            edges.add(t_id)
        else:
            middle.add(t_id)
    pprint(possible_conns)
    return corners, edges, middle, possible_conns


def find_left_up(matrix, i, j):
    one_left = i - 1
    one_up = j - 1
    left_up = {}
    if one_left >= 0:
        left_up['l'] = matrix[one_left][j]
    if one_up >= 0:
        left_up['u'] = matrix[i][one_up]
    return left_up


def matrix_tile(corners, edges, middle, possible_conns, tiles):
    side = int(math.sqrt(len(tiles)))
    matrix = []
    for i in range(side):
        matrix.append([])
        for j in range(side):
            matrix[i].append(0)
    matrix[0][0] = corners.pop()
    matrix[1][0] = possible_conns[matrix[0][0]].pop()
    matrix[0][1] = possible_conns[matrix[0][0]].pop()
    del possible_conns[matrix[0][0]]
    for i in range(side):
        for j in range(side):
            if matrix[i][j] != 0:
                for t_id in possible_conns:
                    if matrix[i][j] in possible_conns[t_id]:
                        possible_conns[t_id].remove(matrix[i][j])
                continue
            lu = find_left_up(matrix, i, j)
            if 'u' in lu and 'l' in lu:
                new = (possible_conns[lu['u']] & possible_conns[lu['l']]).pop()
            elif 'u' in lu and (j != side - 1):
                new = (possible_conns[lu['u']] & edges).pop()
            elif 'u' in lu and (j == side - 1):
                new = (possible_conns[lu['u']] & corners).pop()
            elif 'l' in lu and i != side - 1:
                new = (possible_conns[lu['l']] & edges).pop()
            elif 'l' in lu and i == side - 1:
                new = (possible_conns[lu['l']] & corners).pop()
            matrix[i][j] = new
            for t_id in possible_conns:
                if matrix[i][j] in possible_conns[t_id]:
                    possible_conns[t_id].remove(matrix[i][j])
    return matrix


def find_sides(matrix, i, j, tiles_to_borders):
    side = len(matrix)
    neighbors = {
        'u': None,
        'l': None,
        'r': None,
        'd': None
    }
    if i > 0:
        neighbors['l'] = matrix[i - 1][j]
    if j > 0:
        neighbors['u'] = matrix[i][j - 1]
    if i < side - 1:
        neighbors['r'] = matrix[i + 1][j]
    if j < side - 1:
        neighbors['d'] = matrix[i][j + 1]
    sides = {}
    borders = tiles_to_borders[matrix[i][j]]
    for s, tile_id in neighbors.items():
        if tile_id:
            neighbor_borders = tiles_to_borders[tile_id]
            sides[s] = set(borders).intersection(set(neighbor_borders))
    return sides


def stitch_map(tiles, matrix, tile_to_borders, border_freq):
    side = int(math.sqrt(len(tiles)))
    right_side = {0, 2, 4, 6}
    flip_ltr = {1, 3, 4, 6}
    flip_ud = {0, 2, 5, 7}
    flip_mirror = {1, 3, 5, 7}
    final_map = []
    possible_sides = {}
    possible_orientations = {}
    for i in range(side):
        for j in range(side):
            tile_id = matrix[i][j]
            possible_sides[tile_id] = find_sides(matrix, i, j, tile_to_borders)
            my_borders = tile_to_borders[tile_id]
            if i == 0 and j == 0:
                for k, v in possible_sides[tile_id].items():
                    for b in v:
                        print(my_borders.index(b))


    return possible_sides

def border_to_int(border):
    num = 0
    for i in range(len(border) - 1, -1, -1):
        if border[i] == '#':
            num += 10 ** i
    return num


def tiles_to_borders(tiles):
    borders = {}

    for t_id, t in tiles.items():
        lent = len(t)
        borders[t_id] = [
            border_to_int(t[0]),  # top  0
            border_to_int(t[0][::-1]),  # top reversed 1
            border_to_int(t[-1]),  # bottom 2
            border_to_int(t[-1][::-1]),  # bottom reversed 3
            border_to_int([t[i][0] for i in range(lent)]),  # left 4
            border_to_int([t[i][0] for i in range(lent - 1, -1, -1)]),  # l r 5
            border_to_int([t[i][-1] for i in range(lent)]),  # right 6
            border_to_int([t[i][-1] for i in range(lent - 1, -1, -1)])  # r r 7
        ]
        # T: 0; TR: 1, B: 2, BR: 3, L: 4, LR: 5; R: 6, RR: 7
        # right side: 0, 2, 4, 6
        # flip_ltr: 1, 3, 4, 6
        # flip_ud: 0, 2, 5, 7
        # flip_mirror: 1, 3, 5, 7
    return borders


if __name__ == '__main__':
    with open('src/day20.txt') as fp:
        inputs_ = fp.read()
    tile_id_to_photo = parse_tiles(inputs_.splitlines())
    corners, edges, middle, possible_conns = tiles_in_categories(tile_id_to_photo)
    print(math.prod(corners))
    matrix_of_ids = matrix_tile(corners, edges, middle, possible_conns, tile_id_to_photo)
    pprint(matrix_of_ids)

    t_b = tiles_to_borders(tile_id_to_photo)
    code_frequency = {}
    for t_id, borders_code in t_b.items():
        for code in borders_code:
            if code in code_frequency:
                code_frequency[code].append(t_id)
            else:
                code_frequency[code] = [t_id]

    # pprint(t_b)
    # pprint(code_frequency)

    print(stitch_map(tile_id_to_photo, matrix_of_ids, t_b, code_frequency))
    print('incomplete!')
