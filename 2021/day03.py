import re


def common_bit_at(index, lines, invert=False):
    if sum(1 if line[index] == '1' else -1 for line in lines) >= 0:
        return '1' if not invert else '0'
    else:
        return '0' if not invert else '1'


def common_to_bin_to_dec(lines, invert=False):
    commons = [common_bit_at(i, lines, invert) for i in range(len(lines[0]))]
    return int(''.join(commons), 2)


def sift_by_common_bit(input_lines, invert=False):
    lines = input_lines.copy()
    regex = ''
    while True:
        regex += common_bit_at(len(regex), lines, invert)
        lines = re.findall(f'^{regex}.*$', '\n'.join(lines), re.MULTILINE)
        if len(lines) == 1:
            return int(lines[0], 2)


if __name__ == '__main__':
    with open('src/day03.txt') as fp:
        inputs_ = fp.read()
    inputs_lines = inputs_.splitlines()

    gamma_num = common_to_bin_to_dec(inputs_lines)
    epsilon_num = common_to_bin_to_dec(inputs_lines, invert=True)
    print(gamma_num * epsilon_num)

    o_gen_num = sift_by_common_bit(inputs_lines)
    co2_s_num = sift_by_common_bit(inputs_lines, invert=True)
    print(o_gen_num * co2_s_num)
