if __name__ == '__main__':

    with open('inputs/d01.txt') as fp:
        inputs_ = fp.read()

    calories_carried = [0]
    for row in inputs_.split('\n'):
        if row:
            calories_carried[-1] += int(row)
        else:
            calories_carried.append(0)

    calories_carried.sort(reverse=True)
    print(calories_carried[0])
    print(sum(calories_carried[:3]))
