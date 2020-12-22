def count_trees(lines, dx, dy):
    tree_counter = 0
    j = 0
    for i in range(0, len(lines), dx):
        if lines[i][j] == '#':
            tree_counter += 1

        j += dy
        j %= len(lines[0])
    return tree_counter


if __name__ == '__main__':
    with open('src/day3.txt') as fp:
        lines = [l.strip() for l in fp.readlines()]

        c1 = count_trees(lines, 1, 1)
        c2 = count_trees(lines, 1, 3)
        c3 = count_trees(lines, 1, 5)
        c4 = count_trees(lines, 1, 7)
        c5 = count_trees(lines, 2, 1)
        print(c1 * c2 * c3 * c4 * c5)
