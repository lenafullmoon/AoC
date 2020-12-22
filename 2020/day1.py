def find_3(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])


def find_2(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(numbers[i] * numbers[j])


if __name__ == '__main__':

    with open('src/day1.txt') as fp:
        nums = [int(n.strip()) for n in fp.readlines()]

        find_2(nums)
        find_3(nums)
