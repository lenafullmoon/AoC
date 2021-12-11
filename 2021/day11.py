def get_adjacent(i, j, map_):
    x = [p for p in (i - 1, i, i + 1) if 0 <= p <= len(map_) - 1]
    y = [p for p in (j - 1, j, j + 1) if 0 <= p <= len(map_[0]) - 1]
    neighbours = [(i_, j_) for i_ in x for j_ in y if (i_, j_) != (i, j)]
    return neighbours


if __name__ == '__main__':
    with open('src/day11.txt') as fp:
        inputs_ = fp.read()
    grid = [[int(i) for i in c] for c in inputs_.splitlines()]

    flashes_count = 0
    step = 0
    while True:
        flashes_in_step = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1

        while True:
            to_flash = {(i, j)
                        for i in range(len(grid)) for j in range(len(grid[0]))
                        if grid[i][j] > 9 and (i, j) not in flashes_in_step}
            if not to_flash:
                break
            # do flash
            for (i, j) in to_flash:
                flashes_in_step.add((i, j))
                for (ai, aj) in get_adjacent(i, j, grid):
                    grid[ai][aj] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = 0 if grid[i][j] > 9 else grid[i][j]

        step += 1
        if step <= 100:
            flashes_count += len(flashes_in_step)
        if len(flashes_in_step) == len(grid) * len(grid[0]):
            break
    print(flashes_count)
    print(step)
