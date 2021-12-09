if __name__ == '__main__':
    with open('src/day09.txt') as fp:
        inputs_ = fp.read()
    map_ = [[int(c) for c in line] for line in inputs_.splitlines()]

    solution1_risk_sum = 0
    lowest_coords = []
    for i in range(len(map_)):
        for j in range(len(map_[0])):
            neighbours = []
            if i > 0:
                neighbours.append(map_[i - 1][j])
            if j > 0:
                neighbours.append(map_[i][j - 1])
            if i < len(map_) - 1:
                neighbours.append(map_[i + 1][j])
            if j < len(map_[0]) - 1:
                neighbours.append(map_[i][j + 1])

            if all(map_[i][j] < x for x in neighbours):
                solution1_risk_sum += map_[i][j] + 1
                lowest_coords.append((i, j))
    print(solution1_risk_sum)

    basin_sizes = []
    for low_coord in lowest_coords:
        to_process = [low_coord]
        basin = set()
        while to_process:
            i, j = to_process.pop()
            if (i, j) in basin:
                continue
            basin.add((i, j))
            if i > 0 and map_[i - 1][j] != 9:
                to_process.append((i - 1, j))
            if j > 0 and map_[i][j - 1] != 9:
                to_process.append((i, j - 1))
            if i < len(map_) - 1 and map_[i + 1][j] != 9:
                to_process.append((i + 1, j))
            if j < len(map_[0]) - 1 and map_[i][j + 1] != 9:
                to_process.append((i, j + 1))
        basin_sizes.append(len(basin))
    basin_sizes = sorted(basin_sizes, reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
