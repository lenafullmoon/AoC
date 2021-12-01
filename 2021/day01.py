inputs_ = '''199
200
208
210
200
207
240
269
260
263'''


def count_increases(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
    return count


def sliding_sums(nums):
    return [nums[i] + nums[i + 1] + nums[i + 2]
            for i in range(0, len(nums) - 2)]


if __name__ == '__main__':
    with open('src/day01.txt') as fp:
        inputs_ = fp.read()
    depths = [int(i) for i in inputs_.splitlines()]
    print(count_increases(depths))
    print(count_increases(sliding_sums(depths)))
