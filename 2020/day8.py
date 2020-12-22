JMP, NOP, ACC = 'jmp', 'nop', 'acc'


def parse_op(line):
    op, addr = line.split()
    return op, int(addr)


def do_jmp(acc, nxt_op, addr):
    return acc, nxt_op + addr


def do_nop(acc, nxt_op):
    return acc, nxt_op + 1


def do_acc(acc, nxt_op, addr):
    return acc + addr, nxt_op + 1


def process(op, addr, acc, nxt_op):
    if op == NOP:
        return do_nop(acc, nxt_op)
    if op == ACC:
        return do_acc(acc, nxt_op, addr)
    if op == JMP:
        return do_jmp(acc, nxt_op, addr)


def acc_after_detected_loop(ops):
    accumulator, next_op, executed_ops = 0, 0, []
    while True:
        if next_op >= len(ops):
            break
        if next_op in executed_ops:
            break
        executed_ops.append(next_op)
        op, addr = parse_op(ops[next_op])
        accumulator, next_op = process(op, addr, accumulator, next_op)

    return accumulator


def acc_after_fixed_loop(ops):
    accumulator, next_op, executed_ops, swapped = 0, 0, [], False
    swapped_op = []
    while True:
        if next_op >= len(ops):
            break
        if next_op in executed_ops:
            # start again
            accumulator, next_op, executed_ops, swapped = 0, 0, [], False

        executed_ops.append(next_op)

        op, addr = parse_op(ops[next_op])
        if op == ACC or swapped or next_op in swapped_op:
            accumulator, next_op = process(op, addr, accumulator, next_op)
        else:  # try to fix by swapping nop and jmp
            swapped_op.append(next_op)
            if op == NOP:
                accumulator, next_op = do_jmp(accumulator, next_op, addr)
            if op == JMP:
                accumulator, next_op = do_nop(accumulator, next_op)
            swapped = True
    return accumulator


if __name__ == '__main__':
    with open('src/day8.txt') as fp:
        lines = [line.strip() for line in fp.readlines()]

        print(acc_after_detected_loop(lines))
        print(acc_after_fixed_loop(lines))
