if __name__ == '__main__':
    with open('inputs/d05.txt') as fp:
        inputs_ = fp.read()

    stacks1, stacks2 = {}, {}
    for row in inputs_.splitlines(keepends=False):
        if '[' in row:
            for index, c in enumerate(row):
                if c.isalpha():
                    stack_number = index // 4 + 1
                    stacks1.setdefault(stack_number, []).insert(0, c)
        if not row:
            stacks2 = {k: v.copy() for k, v in stacks1.items()}
        if row.startswith('move'):
            row = row.split()
            amount, from_, to_ = int(row[1]), int(row[3]), int(row[5])
            for i in range(amount):
                stacks1[to_].append(stacks1[from_].pop())
            stacks2[to_].extend(stacks2[from_][-amount:])
            stacks2[from_] = stacks2[from_][:-amount]

    print(''.join(stacks1[i][-1] for i in range(1, len(stacks1) + 1)))
    print(''.join(stacks2[i][-1] for i in range(1, len(stacks2) + 1)))
