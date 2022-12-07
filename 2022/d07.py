if __name__ == '__main__':
    with open('inputs/d07.txt') as fp:
        inputs_ = fp.read()
    tree = {}
    path = []
    dir_sizes = {}
    current_position = None
    for line in inputs_.splitlines(keepends=False):
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd' and line[2] != '..':
                path.append(line[2])
                current_position = tree
                for p in path:
                    current_position.setdefault(p, {})
                    current_position = current_position[p]
                dir_sizes['/'.join(path)] = 0
            elif line[1] == 'cd' and line[2] == '..':
                path.pop()
                current_position = tree
                for p in path:
                    current_position.setdefault(p, {})
                    current_position = current_position[p]
            elif line[1] == 'ls':
                pass
        else:
            if line[0] == 'dir':
                pass
                # current_position[line[1]] = {}
            else:
                current_position[line[1]] = line[0]
                parents = path.copy()
                while parents:
                    dir_sizes['/'.join(parents)] += int(line[0])
                    parents.pop()

    print(sum(size for size in dir_sizes.values() if size <= 100000))

    max_space = 70000000
    target_free_space = 30000000
    free_space = max_space - dir_sizes['/']
    missing_space = target_free_space - free_space
    print(free_space, missing_space)
    size_to_delete = max_space
    for dir_, size in dir_sizes.items():
        if missing_space < size < size_to_delete:
            size_to_delete = size
    print(size_to_delete)
