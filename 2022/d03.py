def priority(c: str):
    return ord(c) - (ord('a') - 1 if c.islower() else ord('A') - 27)


if __name__ == '__main__':
    with open('src/d03.txt') as fp:
        inputs_ = fp.read().split('\n')
    print(sum(priority(
        (set(r[:int(len(r) / 2)]) & set(r[int(len(r) / 2):])).pop()
    ) for r in inputs_))

    print(sum(priority(
        (set(inputs_[i]) & set(inputs_[i + 1]) & set(inputs_[i + 2])).pop()
    ) for i in range(0, len(inputs_), 3)))
