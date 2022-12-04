inputs_ = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

if __name__ == '__main__':
    with open('inputs/d04.txt') as fp:
        inputs_ = fp.read()
    count1 = 0
    count2 = 0
    for pair in inputs_.splitlines(keepends=False):
        range1, range2 = pair.split(',')
        range1 = range1.split('-')
        range2 = range2.split('-')

        if int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
            count1 += 1
            print(pair)
        elif int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]):
            count1 += 1
            print(pair)

        if set(range(int(range1[0]), int(range1[1]) + 1)) & set (range(int(range2[0]), int(range2[1]) + 1)):
            count2+= 1

    print(count1)
    print(count2)

