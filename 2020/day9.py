PREAMBLE_LEN = 25

if __name__ == '__main__':
    with open('src/day9.txt') as fp:
        numbers = [int(line.strip()) for line in fp.readlines()]
    wanted_number = 0
    valid = False
    for n in range(PREAMBLE_LEN, len(numbers)):
        window = numbers[n - PREAMBLE_LEN:n]
        wanted_number = numbers[n]
        for i in range(len(window)):
            for j in range(i, len(window)):
                valid = window[i] + window[j] == wanted_number
                if valid:
                    break
            if valid:
                break
        else:  # not valid
            print(wanted_number)
            break

    found = False
    for group in range(2, len(numbers)):
        for i in range(len(numbers)):
            window = numbers[i: i + group]
            if sum(window) == wanted_number:
                print(min(*window) + max(*window), f'({group})')
                found = True
                break
        if found:
            break
