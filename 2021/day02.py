if __name__ == '__main__':
    with open('src/day02.txt') as fp:
        inputs_ = fp.read()

    horizontal, depth = 0, 0
    horizontal_aim, depth_aim, aim = 0, 0, 0
    for line in inputs_.splitlines():
        direction, number = line.split()
        x = int(number)
        if direction == 'forward':
            horizontal_aim += x
            depth_aim += aim * x
            horizontal += x
        if direction == 'down':
            aim += x
            depth += x
        if direction == 'up':
            aim -= x
            depth -= x

    print(horizontal * depth)
    print(horizontal_aim * depth_aim)
