# nije 1324
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
inputs_ = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#.#^.....
......#.#.
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

    UP.__repr__ = lambda: 'UP'
    DOWN.__repr__ = lambda: 'DN'
    RIGHT.__repr__ = lambda: 'RT'
    LEFT.__repr__ = lambda: 'LT'

    order = [UP, RIGHT, DOWN, LEFT]

    @classmethod
    def turn(cls, direction):
        return cls.order[(cls.order.index(direction) + 1) % len(cls.order)]


class Guard:
    def __init__(self, i, j):
        self.position = Position(i, j)
        self.direction = Direction.UP

    def turn(self):
        self.direction = Direction.turn(self.direction)

    def step(self):
        self.position += self.direction

    def next(self):
        return self.position + self.direction

    def __str__(self):
        return f'{self.position}:'

    def __eq__(self, other):
        return self.position == other.position \
               and self.direction == other.direction

    def __hash__(self):
        return hash((self.position, self.direction))


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
    # with open('inputs/d06.txt') as fp:
    #     inputs_ = fp.read()
    territory = Territory([[row[i] for i in range(len(row))]
                          for row in inputs_.splitlines(keepends=False)])
    obstacle_count = 0
    guard_path_length = 1
    guard_position = territory.starting_position()
    territory[guard_position] = 'X'
    guard_direction = Direction.UP
    position_to_direction = {guard_position: {guard_direction}}
    while territory.in_bounds(guard_position + guard_direction):
        if territory[guard_position + guard_direction] == '#':
            position_to_direction.setdefault(
                guard_position, set()
            ).add(guard_direction)
            guard_direction = Direction.turn(guard_direction)
            continue
        guard_position += guard_direction
        position_to_direction.setdefault(
            guard_position, set()
        ).add(guard_direction)
        guard_path_length += 1 if territory[guard_position] == '.' else 0
        territory[guard_position] = 'X'
        # if I turn right now, do I come by to a path in the same direction
        next_dir = Direction.turn(guard_direction)
        possible_position = Position(guard_position.i, guard_position.j)
        found = False
        print('----', position_to_direction)

        while territory.in_bounds(possible_position + next_dir):
            print(possible_position, next_dir, territory[possible_position])
            if territory[possible_position + next_dir] == '#':
                next_dir = Direction.turn(next_dir)
                continue
            possible_position += next_dir
            if next_dir in position_to_direction.get(possible_position, []):
                found = True
                break
        if found:
            obstacle_count += 1

    print(guard_path_length)
    print(obstacle_count)


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

    UP.__repr__ = lambda: 'UP'
    DOWN.__repr__ = lambda: 'DN'
    RIGHT.__repr__ = lambda: 'RT'
    LEFT.__repr__ = lambda: 'LT'

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
    possible_obstacles = set()
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

        # if I turn right now, do I come by to a path in the same direction
        if guard.next() in possible_obstacles or not territory.in_bounds(guard.next()):
            continue
        swap = territory[guard.next()]
        territory[guard.next()] = '#'
        print(len(possible_obstacles), guard_path_length, guard.next())
        possible_guard = guard.copy()
        possible_guard.turn()
        possible_loop = {possible_guard.copy()}
        while territory.in_bounds(possible_guard.next()):
            # print(possible_guard, territory[possible_guard.position])
            if territory[possible_guard.next()] == '#':
                possible_loop.add(possible_guard.copy())
                possible_guard.turn()
                continue
            possible_guard.step()
            if possible_guard in possible_loop:
                possible_obstacles.add(guard.next())
                # print('obsticle found')
                break
            possible_loop.add(possible_guard.copy())
        # else:
        #     print('out of bounds')
        # print(possible_loop)
        territory[guard.next()] = swap
    print(guard_path_length)
    print(len(possible_obstacles))
    print(possible_obstacles)


# bruteforce


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

    def copy(self):
        return Territory([list(x) for x in self.map])


if __name__ == '__main__':
    # with open('inputs/d06.txt') as fp:
    #     inputs_ = fp.read()
    territory = Territory([[row[i] for i in range(len(row))]
                          for row in inputs_.splitlines(keepends=False)])
    guard_path_length = 1
    guard = Guard(territory.starting_position())
    path = [guard.position]
    while territory.in_bounds(guard.next()):
        if territory[guard.next()] == '#':
            guard.turn()
            continue
        guard.step()
        guard_path_length += 1 if guard.position not in path else 0
        path.append(guard.position)

    print(guard_path_length)

    obs_count = 0
    for i in range(len(territory.map)):
        for j in range(len(territory.map[0])):
            if territory.map[i][j] == '#' or territory.map[i][j] == '^':
                continue
            print(i, j)
            tterr = territory
            swap = tterr.map[i][j]
            tterr.map[i][j] = '#'
            looped = False
            guard = Guard(tterr.starting_position())
            potential_loop = [guard.copy()]
            while tterr.in_bounds(guard.next()):
                if tterr[guard.next()] == '#':
                    guard.turn()
                    continue
                guard.step()
                if guard in potential_loop:
                    looped = True
                    break
                potential_loop.append(guard.copy())
            if looped:
                print('found', i, j)
                obs_count += 1
            tterr.map[i][j] = swap
    print(obs_count)
