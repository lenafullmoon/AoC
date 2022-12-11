if __name__ == '__main__':
    with open('inputs/d11.txt') as fp:
        inputs_ = fp.read().splitlines(keepends=False)

    monkeys = []
    for i in range(0, len(inputs_), 7):
        holding = [int(x) for x in inputs_[i + 1].split(': ')[1].split(', ')]
        operation = inputs_[i + 2].rsplit(' ', 2)[-2:]
        monkeys.append({'holding': holding,
                        'operation': operation,
                        '%': int(inputs_[i + 3].rsplit(' ', 1)[-1]),
                        True: int(inputs_[i + 4].rsplit(' ', 1)[-1]),
                        False: int(inputs_[i + 5].rsplit(' ', 1)[-1])})

    monkey_inspect = [0] * len(monkeys)
    for x in range(20):
        for i, monkey in enumerate(monkeys):
            holding = monkey['holding']
            monkey['holding'] = []
            monkey_inspect[i] += len(holding)
            for item in holding:
                change = monkey['operation'][1]
                change = item if change == 'old' else int(change)
                new_value = ((item + change) if monkey['operation'][0] == '+'
                             else (item * change))
                new_value = new_value // 3
                throw_to = monkey[new_value % monkey['%'] == 0]
                monkeys[throw_to]['holding'].append(new_value)

    monkey_inspect.sort(reverse=True)
    print(monkey_inspect[0] * monkey_inspect[1])
