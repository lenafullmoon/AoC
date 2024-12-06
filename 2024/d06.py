
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


class Position:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Position(self.i + other.i, self.j + other.j)

    def __str__(self):
        return f'({self.i},{self.j})'


class Direction:
    UP = Position(-1, 0)
    RIGHT = Position(0, 1)
    DOWN = Position(1, 0)
    LEFT = Position(0, -1)

    order = [UP, RIGHT, DOWN, LEFT]

    @classmethod
    def next(cls, direction):
        return cls.order[(cls.order.index(direction) + 1) % len(cls.order)]


class Territory:
    def __init__(self, m):
        self.map = m

    def __getitem__(self, position):
        return self.map[position.i][position.j]

    def __setitem__(self, position, value):
        self.map[position.i][position.j] = value

    def in_bounds(self, position):
        return (
            0 <= position.i < len(self.map)
            and 0 <= position.j < len(self.map[0])
        )

    def starting_position(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == '^':
                    return Position(i, j)


if __name__ == '__main__':
    with open('inputs/d06.txt') as fp:
        inputs_ = fp.read()
    territory = Territory([[row[i] for i in range(len(row))]
                          for row in inputs_.splitlines(keepends=False)])

    guard_path_length = 1
    guard_position = territory.starting_position()
    guard_direction = Direction.UP
    while territory.in_bounds(guard_position + guard_direction):
        if territory[guard_position + guard_direction] == '#':
            guard_direction = Direction.next(guard_direction)
            continue
        guard_position += guard_direction
        guard_path_length += 1 if territory[guard_position] == '.' else 0
        territory[guard_position] = 'X'

    print(guard_path_length)
