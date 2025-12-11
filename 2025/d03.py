def max_selection(numbers, sel_len):
    if sel_len == len(numbers):
        return numbers
    if sel_len == 1:
        return str(max(numbers[:]))

    first_digit = str(max(numbers[:-sel_len + 1]))
    fd_index = numbers.index(first_digit)

    return first_digit + max_selection(numbers[fd_index + 1:], sel_len - 1)


if __name__ == '__main__':
    with open('inputs/d03.txt') as fp:
        inputs_ = fp.read()

    total_joltages_2 = 0
    total_joltages_12 = 0
    for row in inputs_.splitlines(keepends=False):
        total_joltages_2 += int(max_selection(row, 2))
        total_joltages_12 += int(max_selection(row, 12))

    print(total_joltages_2)
    print(total_joltages_12)
