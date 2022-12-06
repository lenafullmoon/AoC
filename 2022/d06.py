if __name__ == '__main__':
    with open('inputs/d06.txt') as fp:
        inputs_ = fp.read()
    code = [inputs_[0]] * 4
    for i in range(len(inputs_) - 4):
        code[i % 4] = inputs_[i]
        if len(set(code)) == 4:
            print(i + 1)
            break
    code = [inputs_[0]] * 14
    for i in range(len(inputs_) - 14):
        code[i % 14] = inputs_[i]
        if len(set(code)) == 14:
            print(i + 1)
            break
