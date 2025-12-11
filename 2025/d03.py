
inputs_ = '''987654321111111
811111111111119
234234234234278
818181911112111'''

if __name__ == '__main__':
    with open('inputs/d03.txt') as fp:
        inputs_ = fp.read()
    total_joltages = 0
    for row in inputs_.splitlines(keepends=False):
        max_joltage = 0
        for i in range(0, len(row) - 1):
            for j in range(i + 1, len(row)):
                if int(row[i]+row[j]) > max_joltage:
                    max_joltage = int(row[i]+row[j])
        print(max_joltage)
        total_joltages += max_joltage

    print(total_joltages)
