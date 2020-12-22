
if __name__ == '__main__':
    with open('src/day6.txt') as fp:
        lines = [line.strip() for line in fp.readlines()]

        sum_any = 0
        sum_all = 0
        group_answers_any = set()
        group_answers_all = {
            letter for letter in 'abcdefghijklmnopqrstuvwsxyz'
        }
        for line in lines:
            line_set = {letter for letter in line}
            if line == '':
                sum_any += len(group_answers_any)
                group_answers_any = set()
                sum_all += len(group_answers_all)
                group_answers_all = {
                    letter for letter in 'abcdefghijklmnopqrstuvwsxyz'
                }
            else:
                group_answers_any = group_answers_any.union(line_set)
                group_answers_all = group_answers_all.intersection(line_set)

        else:
            sum_any += len(group_answers_any)
            sum_all += len(group_answers_all)

        print(sum_any, sum_all)
