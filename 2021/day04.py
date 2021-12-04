def find_and_mark_and_signal_win(number, board):
    found_i, found_j = -1, -1
    for i in range(len(board)):
        for j in range(len(board)):
            if number == board[i][j]:
                board[i][j] = -1
                found_i, found_j = i, j
                break
        if found_i > -1 and found_j > -1:
            break
    if found_i > -1 and found_j > -1:
        if all(board[i][found_j] < 0 for i in range(len(board))):
            return True
        if all(board[found_i][j] < 0 for j in range(len(board))):
            return True
    return False


if __name__ == '__main__':
    with open('src/day04.txt') as fp:
        inputs_ = fp.read()
    numbers, *boards = inputs_.split('\n\n')

    boards = [
        [[int(i) for i in c.split()] for c in x.splitlines()] for x in boards
    ]

    index_to_score = {}
    index_won = []
    for num in [int(n) for n in numbers.split(',')]:
        for i in range(len(boards)):
            b = boards[i]
            if find_and_mark_and_signal_win(num, b):
                not_marked = sum(e if e >= 0 else 0 for row in b for e in row)
                if i not in index_won:
                    index_won.append(i)
                    index_to_score[i] = not_marked * num
                if len(index_won) == len(boards):
                    break
        if len(index_won) == len(boards):
            break
    print(index_to_score[index_won[0]])
    print(index_to_score[index_won[-1]])
