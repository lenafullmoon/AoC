def calculate_no_precedence(line):
    def process(x):
        if signs[-1] == '+':
            results[-1] += x
        else:
            results[-1] *= x

    signs = ['+']
    results = [0]
    for i, c in enumerate(line):
        if c == '+' or c == '*':
            signs[-1] = c
        elif c.isdigit():
            process(int(c))
        elif c == '(':
            results.append(0)
            signs.append('+')
        elif c == ')':
            br = results.pop(-1)
            signs.pop(-1)
            process(br)
    return results.pop()


def calculate_precedence_add(line):
    def finalize(br_results, br_signs):
        while len(br_results) > 1:
            x = br_results.pop(-1)
            s = br_signs.pop(-1)
            if s == '+':
                br_results[-1] += x
            else:
                br_results[-1] *= x
        return br_results.pop()

    def process(x):
        if signs[-1][-1] == '+':
            results[-1][-1] += x
            signs[-1].pop(-1)
        else:
            results[-1].append(x)

    signs = [['+']]
    results = [[0]]
    for c in line:
        if c == '+' or c == '*':
            signs[-1].append(c)
        elif c.isdigit():
            process(int(c))
        elif c == '(':
            results.append([0])
            signs.append(['+'])
        elif c == ')':
            br = finalize(results.pop(-1), signs.pop(-1))
            process(br)

    return finalize(results.pop(-1), signs.pop(-1))


if __name__ == '__main__':
    with open('src/day18.txt') as fp:
        inputs_ = fp.read()
    print(sum(calculate_no_precedence(line) for line in inputs_.splitlines()))
    print(sum(calculate_precedence_add(line) for line in inputs_.splitlines()))
