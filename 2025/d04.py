def is_available(x, y, matrix):
    if matrix[x][y] != '@':
        return False
    rolls_around = 0
    start_x = max(0, x - 1)
    end_x = min(x + 2, len(matrix))
    start_y = max(0, y - 1)
    end_y = min(y + 2, len(matrix[0]))
    for cx in range(start_x, end_x):
        for cy in range(start_y, end_y):
            if cx == x and cy == y:
                continue
            if matrix[cx][cy] == '@':
                rolls_around += 1
    return rolls_around < 4


if __name__ == '__main__':
    with open('inputs/d04.txt') as fp:
        inputs_ = fp.read()
    paper_grid = [
        [x for x in row] for row in inputs_.splitlines(keepends=False)
    ]
    print(paper_grid)
    total_available_rolls = 0
    while True:
        available_rolls = 0
        new_grid = [[x for x in row] for row in paper_grid]
        for i in range(len(paper_grid)):
            for j in range(len(paper_grid[0])):
                if is_available(i, j, paper_grid):
                    available_rolls += 1
                    new_grid[i][j] = '.'
        paper_grid = new_grid

        if total_available_rolls == 0:
            print(available_rolls)
        total_available_rolls += available_rolls
        if available_rolls == 0:
            break
    print(total_available_rolls)
