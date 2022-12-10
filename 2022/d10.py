def draw_pixel(cycle, register_value, pixel_matrix):
    coord = (cycle - 1) % 40
    if coord % 40 == 0:
        pixel_matrix.append(['_'] * 40)
    pixel_matrix[-1][coord] = '#' if abs(coord - register) <= 1 else '.'


if __name__ == '__main__':
    with open('inputs/d10.txt') as fp:
        inputs_ = fp.read()

    cycle_number = 0
    register = 1
    solution = 0
    monitor = []
    for row in inputs_.splitlines(keepends=False):
        cycle_number += 1
        draw_pixel(cycle_number, register, monitor)
        solution += (cycle_number * register) if cycle_number % 40 == 20 else 0

        if row == 'noop':
            continue

        cycle_number += 1
        draw_pixel(cycle_number, register, monitor)
        solution += (cycle_number * register) if cycle_number % 40 == 20 else 0

        register += int(row.rsplit(' ')[-1])

    print(solution)
    for line in monitor:
        print(''.join(line))
