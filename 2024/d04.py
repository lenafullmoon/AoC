def count_mas8(crosswords, i, j):
    count = 0
    if j <= len(crosswords[0]) - 4 and (
            crosswords[i][j+1] == 'M' and
            crosswords[i][j+2] == 'A' and
            crosswords[i][j+3] == 'S'
    ):
        count += 1
    if j >= 3 and (
            crosswords[i][j-1] == 'M' and
            crosswords[i][j-2] == 'A' and
            crosswords[i][j-3] == 'S'
    ):
        count += 1
    if i <= len(crosswords) - 4 and (
            crosswords[i+1][j] == 'M' and
            crosswords[i+2][j] == 'A' and
            crosswords[i+3][j] == 'S'
    ):
        count += 1
    if i >= 3 and (
            crosswords[i-1][j] == 'M' and
            crosswords[i-2][j] == 'A' and
            crosswords[i-3][j] == 'S'
    ):
        count += 1

    if j <= len(crosswords[0]) - 4 and i >= 3 and (
            crosswords[i-1][j+1] == 'M' and
            crosswords[i-2][j+2] == 'A' and
            crosswords[i-3][j+3] == 'S'
    ):
        count += 1
    if j >= 3 and i <= len(crosswords) - 4 and (
            crosswords[i+1][j-1] == 'M' and
            crosswords[i+2][j-2] == 'A' and
            crosswords[i+3][j-3] == 'S'
    ):
        count += 1
    if i <= len(crosswords) - 4 and j <= len(crosswords[0]) - 4 and (
            crosswords[i+1][j+1] == 'M' and
            crosswords[i+2][j+2] == 'A' and
            crosswords[i+3][j+3] == 'S'
    ):
        count += 1
    if i >= 3 and j >= 3 and (
            crosswords[i-1][j-1] == 'M' and
            crosswords[i-2][j-2] == 'A' and
            crosswords[i-3][j-3] == 'S'
    ):
        count += 1

    return count


def count_x_mas(crosswords, i, j):
    if i == 0 or i == len(crosswords) - 1 \
            or j == 0 or j == len(crosswords[0]) - 1:
        return 0
    count = 0
    if (
            crosswords[i-1][j-1] == 'M' and
            crosswords[i-1][j+1] == 'M' and
            crosswords[i+1][j-1] == 'S' and
            crosswords[i+1][j+1] == 'S'
    ):
        count += 1
    if (
            crosswords[i+1][j-1] == 'M' and
            crosswords[i+1][j+1] == 'M' and
            crosswords[i-1][j-1] == 'S' and
            crosswords[i-1][j+1] == 'S'
    ):
        count += 1
    if (
            crosswords[i-1][j+1] == 'M' and
            crosswords[i+1][j+1] == 'M' and
            crosswords[i-1][j-1] == 'S' and
            crosswords[i+1][j-1] == 'S'
    ):
        count += 1
    if (
            crosswords[i-1][j-1] == 'M' and
            crosswords[i+1][j-1] == 'M' and
            crosswords[i-1][j+1] == 'S' and
            crosswords[i+1][j+1] == 'S'
    ):
        count += 1

    return count


if __name__ == '__main__':
    with open('inputs/d04.txt') as fp:
        inputs_ = fp.read()
    crosswords = [[row[i] for i in range(len(row))]
                  for row in inputs_.splitlines(keepends=False)]

    match_xmas_count = 0
    match_x_mas_count = 0
    for i in range(len(crosswords)):
        for j in range(len(crosswords[0])):
            if crosswords[i][j] == 'X':
                match_xmas_count += count_mas8(crosswords, i, j)
            if crosswords[i][j] == 'A':
                match_x_mas_count += count_x_mas(crosswords, i, j)

    print(match_xmas_count)
    print(match_x_mas_count)
