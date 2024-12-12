
inputs_ = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''


class Position:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Position(self.i + other.i, self.j + other.j)

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

    def parameter(self, terr):
        borders = set()
        for pos in self.positions:
            for d in Direction.order:
                if terr.in_bounds(pos + d) and terr[pos + d] == self.name:
                    continue
                borders.add((pos, d))
        return len(borders)


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
