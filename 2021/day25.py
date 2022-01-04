def slug_go(direction, slugs, new_i=lambda x: x, new_j=lambda x: x):
    go = []
    for i in range(len(slugs)):
        for j in range(len(slugs[0])):
            if slugs[i][j] == direction:
                if slugs[new_i(i)][new_j(j)] == '.':
                    go.append((i, j))
    for (i, j) in go:
        slugs[i][j] = '.'
        slugs[new_i(i)][new_j(j)] = direction
    return go


if __name__ == '__main__':
    with open('src/day25.txt') as fp:
        inputs_ = fp.read()
    cucumbers = [[x for x in line] for line in inputs_.splitlines()]
    step = 0
    while True:
        step += 1
        to_east = slug_go('>', cucumbers,
                          new_j=lambda x: (x + 1) % len(cucumbers[0]))

        to_south = slug_go('v', cucumbers,
                           new_i=lambda x: (x + 1) % len(cucumbers))

        if not to_east and not to_south:
            break
    print(step)
