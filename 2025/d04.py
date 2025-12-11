
inputs_ = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

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
    paper_grid = inputs_.splitlines(keepends=False)
    available_rolls = 0
    for i in range(len(paper_grid)):
        for j in range(len(paper_grid[0])):
            if is_available(i, j, paper_grid):
                available_rolls += 1

    print(available_rolls)