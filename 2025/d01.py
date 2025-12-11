# TODO awful, fix

if __name__ == '__main__':
    with open('inputs/d01.txt') as fp:
        inputs_ = fp.read()
    dial = 50
    counter_reg = 0
    counter_434 = 0
    for row in inputs_.splitlines(keepends=False):
        inc = 0
        if row[0] == 'L':
            inc = -1
        if row[0] == 'R':
            inc = 1
        for _ in range(int(row[1:])):
            dial += inc
            dial %= 100
            if dial == 0:
                counter_434 += 1
        if dial == 0:
            counter_reg += 1

    print(counter_reg)
    print(counter_434)
