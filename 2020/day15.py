inputs = '''16,12,1,0,15,7,11'''


def slow(ins):
    nums = [int(i) for i in ins.split(',')]
    new_nums = len(nums)
    for i in range(new_nums, 2020):
        if nums.count(nums[-1]) == 1:
            nums.append(0)
        else:
            last_index = -1
            for li in reversed(range(len(nums) - 1)):
                if nums[li] == nums[-1]:
                    last_index = li
                    break
            nums.append(i - 1 - last_index)
    return nums[-1]


def fast(ins, big = 30000000):
    nums = [int(i) for i in ins.split(',')]
    last_indexes = {}
    for i, n in enumerate(nums):
        last_indexes[n] = [i]
    new_nums_from = len(nums)
    last_num = nums[-1]
    for i in range(new_nums_from, big):
        if len(last_indexes[last_num]) == 1:
            new_number = 0
        else:
            last_index = last_indexes[last_num][-2]
            new_number = i - 1 - last_index
        if new_number not in last_indexes:
            last_indexes[new_number] = []
        last_indexes[new_number].append(i)
        last_indexes[new_number] = last_indexes[new_number][-2:]
        last_num = new_number

    return last_num


if __name__ == '''__main__''':
    print(slow(inputs))
    print(fast(inputs))
