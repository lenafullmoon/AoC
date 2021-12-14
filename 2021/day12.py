def r_paths_1(start, paths, caves, path):
    if start.islower() and start in path:
        return
    path = path.copy()
    path.append(start)
    if start == 'end':
        return paths.add(tuple(path))
    for c in caves[start]:
        r_paths_1(c, paths, caves, path)


def r_paths_2(start, paths, caves, path):
    if (start == 'end' or start == 'start') and start in path:
        return
    if start.islower() and start in path and path[0] != 'open':
        return
    path = path.copy()
    path.append(start)

    if start.islower() and path.count(start) == 2:
        path.pop(0)
    if start == 'end':
        return paths.add(tuple(path))
    for cave in caves[start]:
        r_paths_2(cave, paths, caves, path)


if __name__ == '__main__':
    with open('src/day12.txt') as fp:
        inputs_ = fp.read()

    caves_map = {}
    for line in inputs_.splitlines():
        cave1, cave2 = line.split('-')
        caves_map.setdefault(cave1, [])
        caves_map[cave1].append(cave2)
        caves_map.setdefault(cave2, [])
        caves_map[cave2].append(cave1)

    paths_1 = set()
    r_paths_1('start', paths_1, caves_map, [])
    print(len(paths_1))

    paths_2 = set()
    r_paths_2('start', paths_2, caves_map, ['open'])
    print(len(paths_2))
