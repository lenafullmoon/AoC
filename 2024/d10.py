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


def peaks_from(p, terr: Territory):
    peak_count = 0
    peak_positions = set()
    if terr[p] == 9:
        peak_count += 1
        peak_positions.add(p)
    else:
        for direction in Direction.order:
            if terr.in_bounds(p + direction):
                if terr[p + direction] == terr[p] + 1:
                    pcount, pfound = peaks_from(p + direction, terr)
                    peak_count += pcount
                    peak_positions = peak_positions.union(pfound)

    return peak_count, peak_positions


if __name__ == '__main__':
    with open('inputs/d10.txt') as fp:
        inputs_ = fp.read()

    territory = Territory([[int(row[i]) for i in range(len(row))]
                          for row in inputs_.splitlines(keepends=False)])

    peak_sum = 0
    rating_sum = 0
    for i in range(len(territory.map)):
        for j in range(len(territory.map[0])):
            if territory.map[i][j] == 0:
                rating, peaks = peaks_from(Position(i, j), territory)
                rating_sum += rating
                peak_sum += len(peaks)

    print(peak_sum)
    print(rating_sum)
