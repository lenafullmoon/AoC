class Position:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Position(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return Position(self.i - other.i, self.j - other.j)

    def __repr__(self):
        return f'({self.i}, {self.j})'

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

    def __iter__(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                yield Position(i, j)


class Region:
    def __init__(self, name):
        self.name = name
        self.positions = set()

    def area(self):
        return len(self.positions)

    def borders(self, terr):
        borders = {}
        for pos in self.positions:
            for d in Direction.order:
                if terr.in_bounds(pos + d) and terr[pos + d] == self.name:
                    continue
                if pos not in borders:
                    borders[pos] = []
                borders[pos].append(d)
        return borders

    def parameter(self, terr):
        return sum(len(v) for v in self.borders(terr).values())

    def sides(self, terr):
        borders = self.borders(terr)
        corners_turned = 0
        for pos, fences in borders.items():
            if len(fences) == 4:
                corners_turned += 4
            if len(fences) == 3:
                corners_turned += 2
            if len(fences) == 2 and fences[0] + fences[1] != Position(0, 0):
                corners_turned += 1
            for f in fences:
                if pos + f + Direction.turn(f) in borders:
                    next_border = pos + f + Direction.turn(f)
                    next_border_face = Direction.turn(
                        Direction.turn(Direction.turn(f))
                    )
                    inner_corner = pos - next_border_face
                    if next_border_face in borders[next_border]:
                        if (terr.in_bounds(inner_corner)
                                and terr[inner_corner] == terr[pos]):
                            corners_turned += 1

        return corners_turned


def find_region(p, terr: Territory, region=None):
    region = Region(terr[p]) if region is None else region
    region.positions.add(p)
    for d in Direction.order:
        if terr.in_bounds(p + d) and p + d not in region.positions:
            if terr[p + d] == region.name:
                find_region(p + d, terr, region)
    return region


if __name__ == '__main__':
    with open('inputs/d12.txt') as fp:
        inputs_ = fp.read()

    territory = Territory([[row[i] for i in range(len(row))]
                          for row in inputs_.splitlines(keepends=False)])

    regions = []
    assigned_region = set()
    for position in territory:
        if position not in assigned_region:
            new_region = find_region(position, territory)
            regions.append(new_region)
            assigned_region = assigned_region.union(new_region.positions)

    print(sum(region.area() * region.parameter(territory)
              for region in regions))

    print(sum(region.area() * region.sides(territory)
              for region in regions))
