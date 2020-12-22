def to_36bin_str(value):
    bin_str = bin(value)[2:]
    return '0' * (36-len(bin_str)) + bin_str


def apply_mask(value, mask):
    new_value = 0
    for b, m, i in zip(value, mask, range(len(mask))):
        if (m == 'X' and b == '1') or m == '1':
            new_value += 2 ** (len(mask) - i - 1)
    return new_value


def calc_addrs(addr, mask):
    addresses = []
    new_addr = []
    for a, m, i in zip(addr, mask, range(len(mask))):
        if (m == '0' and a == '1') or m == '1':
            new_addr.append('1')
        elif m == 'X':
            new_addr.append('X')
        else:
            new_addr.append('0')

    indices = [i for i, x in enumerate(new_addr) if x == 'X']
    x_count = len(indices)
    for i in range(2 ** x_count):
        replace_with = bin(i)[2:]
        replace_with = '0' * (x_count-len(replace_with)) + replace_with
        floating_addr = new_addr.copy()
        for c, ind in zip(replace_with, indices):
            floating_addr[ind] = c
        addresses.append(int(''.join(floating_addr), 2))
    return addresses


def emulator_v1(lines):
    mem = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in lines:
        var, value = line.split(' = ')
        if var.startswith('mask'):
            mask = value
        else:
            mem_addr = int(var[4:-1])
            value = int(value)
            mem[mem_addr] = apply_mask(to_36bin_str(value), mask)
    return sum(mem.values())


def emulator_v2(lines):
    mem = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in lines:
        var, value = line.split(' = ')
        if var.startswith('mask'):
            mask = value
        else:
            mem_addr = int(var[4:-1])
            value = int(value)
            addrs = calc_addrs(to_36bin_str(mem_addr), mask)
            for addr in addrs:
                mem[addr] = value
    return sum(mem.values())


if __name__ == '__main__':
    with open('src/day14.txt') as fp:
        input_ = fp.read()
    print(emulator_v1(input_.splitlines()))
    print(emulator_v2(input_.splitlines()))
