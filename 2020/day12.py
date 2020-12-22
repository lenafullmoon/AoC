def move(direction, amount, x, y):
    if direction == 'E':
        x += amount
    if direction == 'W':
        x -= amount
    if direction == 'N':
        y += amount
    if direction == 'S':
        y -= amount
    return x, y


def turn(start_dir, degrees):
    dirs = 'NESW'
    return dirs[(dirs.index(start_dir) + degrees//90) % len(dirs)]


def sail_ship(orders):
    ship_direction = 'E'
    x, y = 0, 0
    for o in orders:
        amount = int(o[1:])
        if o[0] == 'F':
            x, y = move(ship_direction, amount, x, y)
        elif o[0] == 'L':
            ship_direction = turn(ship_direction, -amount)
        elif o[0] == 'R':
            ship_direction = turn(ship_direction, amount)
        else:
            x, y = move(o[0], amount, x, y)
    return x, y


def rotate(x, y, amount):
    amount = (amount//90) % 4
    if amount % 2 == 1:
        x, y = y, x
    if amount == 2:
        x, y = -x, -y
    elif amount == 1:
        y = -y
    elif amount == 3:
        x = -x
    return x, y


def sail_with_waypoint(orders):
    x, y = 0, 0
    wp_x, wp_y = 10, 1
    for o in orders:
        amount = int(o[1:])
        if o[0] == 'F':
            x += amount * wp_x
            y += amount * wp_y
        elif o[0] == 'L':
            wp_x, wp_y = rotate(wp_x, wp_y, -amount)
        elif o[0] == 'R':
            wp_x, wp_y = rotate(wp_x, wp_y, amount)
        else:
            wp_x, wp_y = move(o[0], amount, wp_x, wp_y)
    return x, y


def manhattan_distance(x, y):
    return abs(x) + abs(y)


if __name__ == '__main__':
    with open('src/day12.txt') as fp:
        inp = fp.readlines()
    print(manhattan_distance(*sail_ship(inp)))
    print(manhattan_distance(*sail_with_waypoint(inp)))
