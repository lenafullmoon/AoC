if __name__ == '__main__':
    with open('src/day06.txt') as fp:
        inputs_ = fp.read()

    solution_1_initial = [int(i) for i in inputs_.split(',')]
    for _ in range(80):
        zero_count = solution_1_initial.count(0)
        for fish_index in range(len(solution_1_initial)):
            if solution_1_initial[fish_index] == 0:
                solution_1_initial[fish_index] = 7
            solution_1_initial[fish_index] -= 1
        solution_1_initial.extend([8] * zero_count)
    print(len(solution_1_initial))

    solution_2_initial = [int(i) for i in inputs_.split(',')]
    age_to_count = {a: solution_2_initial.count(a) for a in range(9)}
    for _ in range(256):
        zero_count = age_to_count[0]
        for age in range(8):
            age_to_count[age] = age_to_count[age + 1]
        age_to_count[6] += zero_count
        age_to_count[8] = zero_count
    print(sum(age_to_count.values()))
