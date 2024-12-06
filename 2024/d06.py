
inputs_ = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

if __name__ == '__main__':
    with open('inputs/d06.txt') as fp:
        inputs_ = fp.read()
    territory = [[row[i] for i in range(len(row))]
                 for row in inputs_.splitlines(keepends=False)]

    guard_start_position = (-1, -1)
    for i in range(len(territory)):
        for j in range(len(territory[0])):
            if territory[i][j] == '^':
                guard_start_position = (i, j)
                break
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    guard_direction_index = -1
    guard_path_length = 1
    gp = guard_start_position
    while True:
        guard_direction_index = (guard_direction_index + 1) % len(directions)
        gd = directions[guard_direction_index]
        while territory[gp[0] + gd[0]][gp[1] + gd[1]] != '#':
            gp = (gp[0] + gd[0], gp[1] + gd[1])
            guard_path_length += 1 if territory[gp[0]][gp[1]] == '.' else 0
            territory[gp[0]][gp[1]] = 'X'

            if (0 > gp[0] + gd[0] or gp[0] + gd[0] >= len(territory)
                    or 0 > gp[1] + gd[1] or gp[1] + gd[1] >= len(
                        territory[0])):
                break

        if (0 > gp[0] + gd[0] or gp[0] + gd[0] >= len(territory)
                or 0 > gp[1] + gd[1] or gp[1] + gd[1] >= len(territory[0])):
            break

    print(guard_path_length)


