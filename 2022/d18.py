
inputs_ = '''
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.strip('\n')


def find_adjecent(x, y, z):
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1)
    ]


if __name__ == '__main__':
    with open('inputs/d18.txt') as fp:
        inputs_ = fp.read()
    cubes = []
    for row in inputs_.splitlines(keepends=False):
        x, y, z = row.split(',')
        x, y, z = int(x), int(y), int(z)
        cubes.append((x, y, z))

    print(cubes)
    total_sides = 0
    for cube in cubes:
        sides = 6
        for adj in find_adjecent(*cube):
            if adj in cubes:
                sides -= 1
        total_sides += sides
    print(total_sides)
