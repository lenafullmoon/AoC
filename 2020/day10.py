def find_diffs(numbers):
    count_1, count_3 = 0, 0
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] == 1:
            count_1 += 1
        if numbers[i + 1] - numbers[i] == 3:
            count_3 += 1
    return count_1 * count_3


def count_tree(tree, already_calculated):
    if tree == {}:
        return 1
    count = 0
    for k in tree.keys():
        if k not in already_calculated:
            ct = count_tree(tree[k], already_calculated)
            already_calculated[k] = ct
            count += count_tree(tree[k], already_calculated)
        else:
            count += already_calculated[k]
    return count


def small_tree(num, already_built, numbers):
    index = numbers.index(num) + 1
    tree = {num: {}}
    while numbers[index] < device_jolatge and numbers[index] - num < 4:
        if numbers[index] not in already_built:
            st = small_tree(numbers[index], already_built, numbers)
            already_built[numbers[index]] = st[numbers[index]]
            tree[num][numbers[index]] = st[numbers[index]]
        else:
            tree[num][numbers[index]] = already_built[numbers[index]]
        index += 1
    return tree


if __name__ == '__main__':
    with open('src/day10.txt') as fp:
        nums = [int(line.strip()) for line in fp.readlines()]
        nums.append(0)

    nums.sort()
    max_adapter = nums[-1]
    device_jolatge = nums[-1] + 3
    nums.append(device_jolatge)

    print(find_diffs(nums))

    # TODO merge these two recursions
    print(
        count_tree(
            small_tree(0, already_built={}, numbers=nums),
            already_calculated={}
        )
    )
