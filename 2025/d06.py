
inputs_ = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

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
            prod = 1
            for i in range(len(math)-1):
                prod *= int(math[i][col])
            grand_total += prod
    print(grand_total)
