def win_for(move):
    return 'S' if move == 'R' else 'R' if move == 'P' else 'P'


def decipher(c):
    return 'R' if c in 'XA' else 'P' if c in 'YB' else 'S'


def score(opponent, me):
    points = 6 if win_for(me) == opponent else 3 if me == opponent else 0
    return points + (1 if me == 'R' else 2 if me == 'P' else 3)


def from_outcome(opponent, outcome):
    return (opponent if outcome == 'Y' else  # y == draw
            win_for(opponent) if outcome == 'X' else  # x == lose
            'RSP'.replace(opponent, '').replace(win_for(opponent), ''))


if __name__ == '__main__':
    with open('src/d02.txt') as fp:
        inputs_ = fp.read()
    points1, points2 = 0, 0
    for row in inputs_.splitlines(keepends=False):
        opponent_move = decipher(row[0])
        points1 += score(opponent_move, decipher(row[2]))
        points2 += score(opponent_move, from_outcome(opponent_move, row[2]))
    print(points1)
    print(points2)
