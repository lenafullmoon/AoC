DIRECTIONS = {
    'U': complex(1, 0),
    'D': complex(-1, 0),
    'L': complex(0, -1),
    'R': complex(0, 1)
}


def trail(target: complex, start: complex):
    if abs(target - start) < 1.5:
        return []
    dirs = []
    if target.real < start.real:
        dirs.append(DIRECTIONS['D'])
    elif target.real > start.real:
        dirs.append(DIRECTIONS['U'])
    if target.imag < start.imag:
        dirs.append(DIRECTIONS['L'])
    elif target.imag > start.imag:
        dirs.append(DIRECTIONS['R'])
    return dirs


if __name__ == '__main__':
    with open('inputs/d09.txt') as fp:
        inputs_ = fp.read()

    snake = [complex(0, 0)] * 10
    tail_trail1 = [complex(0, 0)]
    tail_trail2 = [complex(0, 0)]
    for row in inputs_.splitlines(keepends=False):
        dir_, steps = row.split()

        for _ in range(int(steps)):
            snake[0] += DIRECTIONS[dir_]
            for i in range(1, len(snake)):
                for move in trail(snake[i - 1], snake[i]):
                    snake[i] += move
            tail_trail1.append(snake[1])
            tail_trail2.append(snake[-1])

    print(len(set(tail_trail1)))
    print(len(set(tail_trail2)))
