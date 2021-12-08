LEN_1 = 2  # 'cf'
LEN_2_3_5 = 5  # 'acdeg', 'acdfg', 'abdfg'
LEN_4 = 4  # 'bcdf'
LEN_6_9_0 = 6  # 'abdefg', 'abcdfg', abcefg'
LEN_7 = 3  # 'acf'
LEN_8 = 7  # 'abcdefg'

if __name__ == '__main__':
    with open('src/day08.txt') as fp:
        inputs_ = fp.read()

    solution_1_count_simple = 0
    solution_2_sum_codes = 0
    for line in inputs_.splitlines():
        signal_patters, four_digit_output = line.split(' | ')
        int_to_code = {k: None for k in range(10)}

        for digit in sorted(signal_patters.split(), key=lambda x: len(x)):
            if len(digit) == LEN_1:
                int_to_code[1] = set(digit)
            elif len(digit) == LEN_7:
                int_to_code[7] = set(digit)
            elif len(digit) == LEN_4:
                int_to_code[4] = set(digit)
            elif len(digit) == LEN_8:
                int_to_code[8] = set(digit)
            elif len(digit) == LEN_2_3_5:
                if len(set(digit) - int_to_code[7]) == 2:
                    int_to_code[3] = set(digit)
                elif len(set(digit) - int_to_code[4]) == 2:
                    int_to_code[5] = set(digit)
                else:
                    int_to_code[2] = set(digit)
            elif len(digit) == LEN_6_9_0:
                if len(set(digit) - int_to_code[4]) == 2:
                    int_to_code[9] = set(digit)
                elif len(set(digit) - int_to_code[5]) == 1:
                    int_to_code[6] = set(digit)
                else:
                    int_to_code[0] = set(digit)

        four_digit_code = 0
        for digit in four_digit_output.split():
            if len(digit) in [LEN_1, LEN_4, LEN_7, LEN_8]:
                solution_1_count_simple += 1
            digit = set(digit)
            for i, code in int_to_code.items():
                if code == digit:
                    four_digit_code = four_digit_code * 10 + i
                    break
        solution_2_sum_codes += four_digit_code
    print(solution_1_count_simple)
    print(solution_2_sum_codes)
