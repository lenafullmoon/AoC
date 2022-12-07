def find_current_dir(current_dir, current_path):
    for p in current_path:
        current_dir = current_dir[p]
    return current_dir


if __name__ == '__main__':
    with open('inputs/d07.txt') as fp:
        inputs_ = fp.read()

    tree = {'/': {}}
    dir_sizes = {'/': 0}
    current_position = tree['/']
    path = []
    for line in inputs_.splitlines(keepends=False):
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd' and line[2] != '..':
                path.append(line[2])
                current_position[line[2]] = {}
                current_position = find_current_dir(tree, path)
                dir_sizes['/'.join(path)] = 0
            elif line[1] == 'cd' and line[2] == '..':
                path.pop()
                current_position = find_current_dir(tree, path)
        elif line[0] != 'dir':
            parents = path.copy()
            while parents:
                dir_sizes['/'.join(parents)] += int(line[0])
                parents.pop()

    print(sum(size for size in dir_sizes.values() if size <= 100000))

    MAX_SPACE, TARGET_SPACE = 70000000, 30000000
    missing_space = TARGET_SPACE - (MAX_SPACE - dir_sizes['/'])
    print(min(size for size in dir_sizes.values() if size > missing_space))
