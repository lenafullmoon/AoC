if __name__ == '__main__':

    with open('inputs/d01.txt') as fp:
        inputs_ = fp.read()

    list1 = []
    list2 = []
    for row in inputs_.split('\n'):
        loc1, loc2 = row.split()
        list1.append(int(loc1.strip()))
        list2.append(int(loc2.strip()))

    list1 = sorted(list1)
    list2 = sorted(list2)

    diff_sum = 0
    sim_score = 0
    for sloc1, sloc2 in zip(list1, list2):
        diff_sum += abs(sloc2-sloc1)
        sim_score += sloc1 * list2.count(sloc1)

    print(diff_sum)
    print(sim_score)

