import itertools

operator_combinations = {}


def find_all_operator_combinations(amount, operators):
    key = ''.join(operators) + str(amount)
    if key not in operator_combinations:
        operator_combinations[key] = sorted(
            list(set(itertools.combinations(operators * amount, amount)))
        )

    return operator_combinations[key]


def find_result(target, opers, operators):
    operator_sets = find_all_operator_combinations(len(opers) - 1, operators)
    for operators in operator_sets:
        res = opers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                res += opers[i + 1]
            if operators[i] == '*':
                res *= opers[i + 1]
            if operators[i] == 'u':
                res = int(f'{res}{opers[i + 1]}')
        if res == target:
            return res
    return 0


if __name__ == '__main__':
    with open('inputs/d07.txt') as fp:
        inputs_ = fp.read()
    calibrations = []
    for row in inputs_.splitlines(keepends=False):
        test, operands = row.split(':')
        operands = [int(x.strip()) for x in operands.split()]
        calibrations.append((int(test), operands))

    found_results_2_sum = 0
    found_results_3_sum = 0
    for result, operands in calibrations:
        found_results_2_sum += find_result(result, operands, ['+', '*'])
        found_results_3_sum += find_result(result, operands, ['+', '*', 'u'])

    print(found_results_2_sum)
    print(found_results_3_sum)
