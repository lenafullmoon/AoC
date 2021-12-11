def count_increases(nums):
    return sum(1 for i in range(1, len(nums)) if nums[i] > nums[i - 1])


if __name__ == '__main__':
    with open('src/day01.txt') as fp:
        inputs_ = fp.read()

    depths = [int(i) for i in inputs_.splitlines()]
    print(count_increases(depths))
    print(count_increases([depths[i] + depths[i + 1] + depths[i + 2]
                           for i in range(0, len(depths) - 2)]))
