if __name__ == '__main__':
    with open('src/day07.txt') as fp:
        inputs_ = fp.read()

    positions = [int(i) for i in inputs_.split(',')]

    minimum_fuel = None
    for position in range(max(positions)):
        sum_destination = sum(abs(target - position) for target in positions)
        if minimum_fuel is None or minimum_fuel > sum_destination:
            minimum_fuel = sum_destination
    print(minimum_fuel)

    minimum_fuel = None
    for position in range(max(positions)):
        sum_destination = 0
        for target in positions:
            dst = abs(target - position)
            sum_destination += int((dst * (dst + 1)) / 2)
        if minimum_fuel is None or minimum_fuel > sum_destination:
            minimum_fuel = sum_destination

    print(minimum_fuel)
