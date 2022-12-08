def is_visible(x, y, matrix):
    limit = (0, len(matrix) - 1)
    if x in limit or y in limit:
        return True
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        mx, my = x + direction[0], y + direction[1]
        while matrix[mx][my] < matrix[x][y]:
            if mx in limit or my in limit:
                return True
            mx, my = mx + direction[0], my + direction[1]
    return False


def score(x, y, matrix):
    limit = (0, len(matrix) - 1)
    if x in limit or y in limit:
        return 0
    scenic = []
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        scenic.append(0)
        mx, my = x + direction[0], y + direction[1]
        while True:
            scenic[-1] += 1
            if mx in limit or my in limit or matrix[mx][my] >= matrix[x][y]:
                break
            mx, my = mx + direction[0], my + direction[1]
    return scenic[0] * scenic[1] * scenic[2] * scenic[3]


if __name__ == '__main__':
    with open('inputs/d08.txt') as fp:
        inputs_ = fp.read()

    forrest = [[int(c) for c in x] for x in inputs_.splitlines(keepends=False)]

    visible_coords = set()
    max_scenic = 0
    for i in range(len(forrest)):
        for j in range(len(forrest)):
            if is_visible(i, j, forrest):
                visible_coords.add((i, j))
            max_scenic = max(max_scenic, score(i, j, forrest))

    print(len(visible_coords))
    print(max_scenic)
