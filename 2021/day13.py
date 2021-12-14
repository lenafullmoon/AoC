if __name__ == '__main__':
    with open('src/day13.txt') as fp:
        inputs_ = fp.read()

    coords, folds = inputs_.split('\n\n')
    coords = {(int(line.split(',')[0]), int(line.split(',')[1]))
              for line in coords.splitlines()}
    folds = [(line.split('=')[0], int(line.split('=')[1]))
             for line in [line.split()[-1] for line in folds.splitlines()]]

    for i, fold in enumerate(folds):
        folded = set()
        for coord in coords:
            if fold[0] == 'x' and coord[0] > fold[1]:
                folded.add((coord[0] - 2 * (coord[0] - fold[1]), coord[1]))
            elif fold[0] == 'y' and coord[1] > fold[1]:
                folded.add((coord[0], coord[1] - 2 * (coord[1] - fold[1])))
            else:
                folded.add(coord)
        if i == 0:
            print(len(folded))
        coords = folded

    max_i = max(c[0] for c in coords) + 1
    max_j = max(c[1] for c in coords) + 1
    code = [[' ' if (i, j) not in coords else '█' for i in range(max_i)]
            for j in range(max_j)]
    print('\n'.join([''.join(row) for row in code]))
