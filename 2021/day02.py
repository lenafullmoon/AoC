if __name__ == '__main__':
    with open('src/day02.txt') as fp:
        inputs_ = fp.read()

    horizontal = 0
    depth_1_aim_2 = 0
    depth_2 = 0
    for line in inputs_.splitlines():
        direction, dx = [int(x) if x.isdecimal() else x for x in line.split()]
        if direction == 'forward':
            depth_2 += depth_1_aim_2 * dx
            horizontal += dx
        if direction == 'down':
            depth_1_aim_2 += dx
        if direction == 'up':
            depth_1_aim_2 -= dx

    print(horizontal * depth_1_aim_2)
    print(horizontal * depth_2)
