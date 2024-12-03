import re


if __name__ == '__main__':
    with open('inputs/d03.txt') as fp:
        inputs_ = fp.read()

    re_mul = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't())")

    mul_sum_all = 0
    mul_sum_enabled = 0
    mul_enabled = True
    for match in re_mul.findall(inputs_):
        if match[0]:
            a, b = (int(x) for x in match[0][4:-1].split(','))
            mul_sum_all += a * b
            mul_sum_enabled += a * b if mul_enabled else 0
        if match[1]:
            mul_enabled = True
        if match[2]:
            mul_enabled = False

    print(mul_sum_all)
    print(mul_sum_enabled)
