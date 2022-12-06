def find_start_code(inputs, code_length):
    code_buffer = [inputs[0]] * code_length
    for i in range(len(inputs) - code_length):
        code_buffer[i % code_length] = inputs[i]
        if len(set(code_buffer)) == code_length:
            return i + 1


if __name__ == '__main__':
    with open('inputs/d06.txt') as fp:
        inputs_ = fp.read()

    print(find_start_code(inputs_, code_length=4))  # package start
    print(find_start_code(inputs_, code_length=14))  # message start
