def add_counts(count_1, count_2):
    for k, v in count_2.items():
        if k not in count_1:
            count_1[k] = 0
        count_1[k] += v


def solution2_r(subs, cache, first, second, step, steps=40):
    if step == steps:
        return {}
    if (first, second, step) in cache:
        return cache[(first, second, step)]
    insert = subs[''.join((first, second))]
    my_counts = {insert: 1}
    l_count = solution2_r(subs, cache, first, insert, step + 1, steps)
    r_count = solution2_r(subs, cache, insert, second, step + 1, steps)
    add_counts(my_counts, l_count)
    add_counts(my_counts, r_count)
    cache[(first, second, step)] = my_counts
    return my_counts


def solution2(polymer, subs, steps):
    counts = {polymer[0]: 1}
    counts_cache = {}
    for i, el in enumerate(polymer[:-1]):
        pair_count = solution2_r(subs, counts_cache, el, polymer[i + 1],
                                 0, steps)
        add_counts(counts, pair_count)
        add_counts(counts, {polymer[i + 1]: 1})
    counts_2 = sorted(counts.values())
    return counts_2[-1] - counts_2[0]


if __name__ == '__main__':
    with open('src/day14.txt') as fp:
        inputs_ = fp.read()

    polymer_start, substitutions = inputs_.split('\n\n')
    substitutions = {line.split(' -> ')[0]: line.split(' -> ')[1]
                     for line in substitutions.splitlines()}

    print(solution2(polymer_start, substitutions, 10))
    print(solution2(polymer_start, substitutions, 40))

# ------------------ line count to here ------------------------------------ #


def solution1(polymer, subs, steps=10):
    for _ in range(steps):
        new_polymer = [polymer[0]]
        for i, el in enumerate(polymer):
            if i == len(polymer) - 1:
                break
            new_polymer.append(subs[''.join([el, polymer[i + 1]])])
            new_polymer.append(polymer[i + 1])
        polymer = new_polymer
    counts_1 = sorted(polymer.count(v) for v in subs.values())
    return counts_1[-1] - counts_1[0]
