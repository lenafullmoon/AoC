
inputs_ = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''


def distance(point1, point2):
    a = point1[0] - point2[0]
    b = point1[1] - point2[1]
    c = point1[2] - point2[2]
    return (a ** 2 + b ** 2 + c ** 2) ** 0.5


if __name__ == '__main__':
    with open('inputs/d08.txt') as fp:
        inputs_ = fp.read()
    boxes = []
    for row in inputs_.splitlines(keepends=False):
        boxes.append(tuple(int(x) for x in row.split(',')))

    distances = []
    for i in range(len(boxes) -  1):
        for j in range(i + 1, len(boxes)):
            box1 = boxes[i]
            box2 = boxes[j]
            distances.append((i, j, distance(box1, box2)))

    distances.sort(key=lambda x: x[2])
    print(distances)

    circuits = [{x} for x in range(len(boxes))]
    brk = 0
    for d in distances:
        brk += 1
        extended1 = None
        extended2 = None
        for i in range(len(circuits)):
            if d[0] in circuits[i]:
                extended1 = i
            if d[1] in circuits[i]:
                extended2 = i
        if extended2 != extended1:
            c1 = circuits.pop(max(extended1, extended2))
            c2 = circuits.pop(min(extended1, extended2))
            circuits.append(c2.union(c1))
        if brk == 1000:
            break

    circuits.sort(key=lambda x: len(x), reverse=True)
    print(circuits)
    print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
