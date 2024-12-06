
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

    def __sub__(self, other):
        return Position(self.i - other.i, self.j - other.j)

    def __repr__(self):
        return f'({self.i},{self.j})'

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash((self.i, self.j))


class Direction:
    UP = Position(-1, 0)
    RIGHT = Position(0, 1)
    DOWN = Position(1, 0)
    LEFT = Position(0, -1)

    order = [UP, RIGHT, DOWN, LEFT]

    @classmethod
    def turn(cls, direction):
        return cls.order[(cls.order.index(direction) + 1) % len(cls.order)]


class Guard:
    def __init__(self, position):
        self.position = position
        self.direction = Direction.UP

    def turn(self):
        self.direction = Direction.turn(self.direction)

    def step(self):
        self.position += self.direction

    def next(self):
        return self.position + self.direction

    def __repr__(self):
        return f'{self.position}:{self.direction}'

    def __eq__(self, other):
        return self.position == other.position \
               and self.direction == other.direction

    def __hash__(self):
        return hash((self.position, self.direction))

    def copy(self):
        new_guard = Guard(Position(self.position.i, self.position.j))
        new_guard.direction = self.direction
        return new_guard


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
    guard = Guard(territory.starting_position())
    territory[guard.position] = 'X'

    while territory.in_bounds(guard.next()):
        if territory[guard.next()] == '#':
            guard.turn()
            continue
        guard.step()
        guard_path_length += 1 if territory[guard.position] == '.' else 0
        territory[guard.position] = 'X'

    print(guard_path_length)
