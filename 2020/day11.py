from copy import deepcopy


def occupied_around(x, y, current_seats):
    max_x, max_y = len(current_seats),  len(current_seats[0])
    occupied = 0
    for i in range(max(0, x-1), min(max_x, x + 2)):
        for j in range(max(0, y-1), min(max_y, y + 2)):
            if not (x == i and y == j) and current_seats[i][j] == '#':
                occupied += 1
    return occupied


def count(direction, x, y, current_seats):
    max_x, max_y = len(current_seats),  len(current_seats[0])

    i, j = x, y
    occupied = 0
    should_break = False
    while True:
        if 'u' in direction:
            should_break |= i == 0
            i = max(0, i - 1)
        if 'd' in direction:
            should_break |= i == max_x - 1
            i = min(max_x - 1, i + 1)
        if 'l' in direction:
            should_break |= j == 0
            j = max(0, j - 1)
        if 'r' in direction:
            should_break |= j == max_y - 1
            j = min(max_y - 1, j + 1)
        if (i == x and y == j) or should_break:
            break
        if current_seats[i][j] == '#':
            occupied += 1
        if current_seats[i][j] != '.':
            break
    return occupied


def occupied_directions(x, y, current_seats):
    occupied = 0
    for direction in ['u', 'd', 'l', 'r', 'ur', 'ul', 'dr', 'dl']:
        occupied += count(direction, x, y, current_seats)
    return occupied


def find_stable_seats(seats, too_much, occ_counter):
    new_seats = deepcopy(seats)
    while True:
        old_seats = deepcopy(new_seats)
        change_made = False
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                curr_seat = old_seats[i][j]
                if curr_seat == '.':
                    continue
                occ_count = occ_counter(i, j, old_seats)
                if curr_seat == 'L' and occ_count == 0:
                    new_seats[i][j] = '#'
                    change_made = True
                elif curr_seat == '#' and occ_count >= too_much:
                    new_seats[i][j] = 'L'
                    change_made = True
        if not change_made:
            break
    return new_seats


if __name__ == '__main__':
    with open('src/day11.txt') as fp:
        empty_seats = [[c for c in line.strip()] for line in fp.readlines()]
    stable1 = find_stable_seats(empty_seats, too_much=4,
                                occ_counter=occupied_around)
    print(sum([row.count('#') for row in stable1]))
    stable2 = find_stable_seats(empty_seats, too_much=5,
                                occ_counter=occupied_directions)
    print(sum([row.count('#') for row in stable2]))
