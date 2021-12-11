def find_and_mark_and_signal_win(number, board):
    found = [(i, j) for i in range(len(board)) for j in range(len(board[0]))
             if number == board[i][j]]
    if not found:
        return False
    x, y = found[0]
    board[x][y] = -1
    return (
        all(board[i][y] < 0 for i in range(len(board))) or
        all(board[x][j] < 0 for j in range(len(board[0])))
    )


if __name__ == '__main__':
    with open('src/day04.txt') as fp:
        inputs_ = fp.read()

    numbers, *boards = inputs_.split('\n\n')
    boards = [
        [[int(i) for i in c.split()] for c in x.splitlines()] for x in boards
    ]

    wins = set()
    scores = []
    for num in [int(n) for n in numbers.split(',')]:
        for i, b in enumerate(boards):
            if len(scores) == len(numbers):
                break
            if i not in wins and find_and_mark_and_signal_win(num, b):
                wins.add(i)
                scores.append(sum(e for row in b for e in row if e > 0) * num)

    print(scores[0])
    print(scores[-1])
