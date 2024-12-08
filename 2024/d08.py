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

    def copy(self):
        return Position(self.i, self.j)


class Territory:
    def __init__(self, m):
        self.map = m

    def in_bounds(self, position):
        return (
            0 <= position.i < len(self.map)
            and 0 <= position.j < len(self.map[0])
        )


if __name__ == '__main__':
    with open('inputs/d08.txt') as fp:
        inputs_ = fp.read()

    territory = Territory([[row[i] for i in range(len(row))]
                          for row in inputs_.splitlines(keepends=False)])

    antenae = {}
    for i in range(len(territory.map)):
        for j in range(len(territory.map[0])):
            if territory.map[i][j] == '.':
                continue
            antenae.setdefault(territory.map[i][j], []).append(Position(i, j))

    antinodes_simple_harmonics = set()
    antinodes_resonant_harmonics = set()
    for _, positions in antenae.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                a = positions[i].copy()
                b = positions[j].copy()
                diff = a - b

                if territory.in_bounds(a + diff):
                    antinodes_simple_harmonics.add(a + diff)
                if territory.in_bounds(b - diff):
                    antinodes_simple_harmonics.add(b - diff)

                antinodes_resonant_harmonics.add(a)
                antinodes_resonant_harmonics.add(b)
                while territory.in_bounds(a + diff):
                    antinodes_resonant_harmonics.add(a + diff)
                    a += diff
                while territory.in_bounds(b - diff):
                    antinodes_resonant_harmonics.add(b - diff)
                    b -= diff

    print(len(antinodes_simple_harmonics))
    print(len(antinodes_resonant_harmonics))
