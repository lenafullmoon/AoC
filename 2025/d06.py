def prod(itr):
    p = 1
    for x in itr:
        p *= x
    return p


if __name__ == '__main__':
    with open('inputs/d06.txt') as fp:
        inputs_ = fp.read()
    math = []
    for row in inputs_.splitlines(keepends=False):
        math.append([x for x in row.split(" ") if x != ''])

    grand_total = 0
    for col in range(len(math[0])):

        if math[-1][col] == '+':
            grand_total += sum(int(math[i][col]) for i in range(len(math)-1))

        if math[-1][col] == '*':
            grand_total += prod(int(math[i][col]) for i in range(len(math)-1))
    print(grand_total)

    math = []
    for row in inputs_.splitlines(keepends=False):
        math.append([x for x in row])

    grand_total = 0
    operator = None
    column_numbers = []
    for col in range(len(math[0])):
        number = 0
        pow = 0

        for i in range(len(math) - 1, -1, -1):
            col_safe = col < len(math[i])
            if i == len(math) - 1 and col_safe and math[i][col] != ' ':
                operator = math[i][col]
            if col_safe and math[i][col] != ' ' and i < len(math) - 1:
                number += int(math[i][col]) * 10 ** pow
                pow += 1
        if number != 0:
            column_numbers.append(number)
        if number == 0 or col == len(math[0]) - 1:
            if operator == '*':
                grand_total += prod(column_numbers)
            elif operator == '+':
                grand_total += sum(column_numbers)

            operator = None
            column_numbers = []
    print(grand_total)
