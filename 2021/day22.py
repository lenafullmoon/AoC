def return_range(rng_string):
    dot = rng_string.index('.')
    start = int(rng_string[2: dot])
    end = int(rng_string[dot + 2:])
    return range(start, end + 1)


def return_cuboids(ranges):
    rng_x, rng_y, rng_z = ranges.split(',')
    return return_range(rng_x), return_range(rng_y), return_range(rng_z)


def initiation():
    cubes_on = set()
    for line in inputs_.splitlines():
        power, coords = line.split()
        r_x, r_y, r_z = return_cuboids(coords)
        if r_x.start > 50 or r_x.start < -50:
            continue
        for i in r_x:
            for j in r_y:
                for k in r_z:
                    if power == 'on':
                        cubes_on.add((i, j, k))
                    elif (i, j, k) in cubes_on:
                        cubes_on.remove((i, j, k))
    print(len(cubes_on))


if __name__ == '__main__':
    with open('src/day22.txt') as fp:
        inputs_ = fp.read()

    initiation()
