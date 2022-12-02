inputs_ = '''A Y
B X
C Z'''
loses = {'B X', 'A Z', 'C Y'}
draws = {'A X', 'B Y', 'C Z'}

to_win = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

to_lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}


if __name__ == '__main__':
    with open('src/d02.txt') as fp:
        inputs_ = fp.read()
    points = 0
    for row in inputs_.splitlines(keepends=False):
        if row in loses:
            points += 0
        elif row in draws:
            points += 3
        else:
            points += 6
        if row.endswith('X'):
            points += 1
        elif row.endswith('Y'):
            points += 2
        else:
            points += 3
    print(points)

# X - lose, Y - draw, Z - win
    points = 0
    for row in inputs_.splitlines(keepends=False):
        opponent, outcome = row.split()
        my_choice = None
        if outcome == 'X':
            points += 0
            my_choice = to_lose[opponent]
        elif outcome == 'Y':
            points += 3
            my_choice = opponent
        else:
            points += 6
            my_choice = to_win[opponent]
        if my_choice == 'A':
            points += 1
        elif my_choice == 'B':
            points += 2
        else:
            points += 3

    print(points)

