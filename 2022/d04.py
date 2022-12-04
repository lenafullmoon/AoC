if __name__ == '__main__':
    with open('inputs/d04.txt') as fp:
        inputs_ = fp.read()

    res_1, res_2 = 0, 0
    for pair in inputs_.splitlines(keepends=False):
        cleaning_range1, cleaning_range2 = pair.split(',')
        cleaning_range1 = [int(limit) for limit in cleaning_range1.split('-')]
        cleaning_range2 = [int(limit) for limit in cleaning_range2.split('-')]
        areas1 = set(range(cleaning_range1[0], cleaning_range1[1] + 1))
        areas2 = set(range(cleaning_range2[0], cleaning_range2[1] + 1))

        res_1 += 1 if not areas1 - areas2 or not areas2 - areas1 else 0
        res_2 += 1 if areas1 & areas2 else 0

    print(res_1)
    print(res_2)
