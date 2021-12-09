if __name__ == '__main__':
    with open('src/day06.txt') as fp:
        inputs_ = fp.read()

    solution_1_initial = [int(i) for i in inputs_.split(',')]
    for day in range(80):
        zero_count = 0
        for fish_index in range(len(solution_1_initial)):
            if solution_1_initial[fish_index] == 0:
                zero_count += 1
                solution_1_initial[fish_index] = 6
            else:
                solution_1_initial[fish_index] -= 1
        solution_1_initial.extend([8] * zero_count)
    print(len(solution_1_initial))

    solution_2_initial = [int(i) for i in inputs_.split(',')]
    ages_to_count = {k: solution_2_initial.count(k) for k in range(9)}
    for day in range(256):
        zero_count = ages_to_count[0]
        for age in range(6):
            ages_to_count[age] = ages_to_count[age + 1]
        ages_to_count[6] = ages_to_count[7] + zero_count
        ages_to_count[7] = ages_to_count[8]
        ages_to_count[8] = zero_count
    print(sum(ages_to_count.values()))
