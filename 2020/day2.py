def parse_line(line):
    # 10-11 t: vttttttpnkhkttpjttt
    nums, letter, password = line.split()
    letter = letter.strip(':')
    n1, n2 = nums.split('-')
    n1, n2 = int(n1), int(n2)

    return n1, n2, letter, password


def is_valid_1(mn, mx, letter, password):
    return mn <= password.count(letter) <= mx


def is_valid_2(pos1, pos2, letter, password):
    pos1 -= 1
    pos2 -= 1
    return (password[pos1] == letter and password[pos2] != letter) or (
            password[pos2] == letter and password[pos1] != letter
    )


if __name__ == '__main__':
    with open('src/day2.txt') as fp:
        lines = [n.strip() for n in fp.readlines()]
    count1 = 0
    count2 = 0
    for line in lines:
        parsed_line = parse_line(line)
        if is_valid_1(*parsed_line):
            count1 += 1
        if is_valid_2(*parsed_line):
            count2 += 1

    print(count1, count2)
