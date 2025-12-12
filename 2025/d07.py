
inputs_ = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''


if __name__ == '__main__':
    with open('inputs/d07.txt') as fp:
        inputs_ = fp.read()
    manifold = []
    for row in inputs_.splitlines(keepends=False):
        manifold.append([x for x in row])

    print(manifold)

    tachyons = [(0, manifold[0].index('S'))]
    split_count = 0
    for i in range(1, len(manifold)):
        new_tachyons = []
        for t in tachyons:
            if manifold[t[0] + 1][t[1]] == '.':
                nt = t[0] + 1, t[1]
                if nt not in new_tachyons:
                    new_tachyons.append(nt)
            else:
                split_count += 1
                nt = t[0]+1, t[1] - 1
                if nt not in new_tachyons:
                    new_tachyons.append(nt)
                nt = t[0]+1, t[1] + 1
                if nt not in new_tachyons:
                    new_tachyons.append(nt)
        tachyons = new_tachyons.copy()
    print(split_count)



