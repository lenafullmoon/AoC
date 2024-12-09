if __name__ == '__main__':
    with open('inputs/d09.txt') as fp:
        inputs_ = fp.read()
    segments = [int(char) for char in inputs_]

    free_spaces = {}
    file_segments = {}
    disk = []
    for i in range(len(segments)):
        if i % 2 == 0:
            file_segments[len(disk)] = segments[i]
            disk.extend([(i + 1) // 2] * segments[i])
        else:
            free_spaces[len(disk)] = segments[i]
            disk.extend(['.'] * segments[i])

    fully_frgm_disk = disk.copy()
    free_i = 0
    file_i = len(fully_frgm_disk.copy()) - 1
    while free_i < file_i:
        if fully_frgm_disk[free_i] != '.':
            free_i += 1
            continue
        if fully_frgm_disk[file_i] == '.':
            file_i -= 1
            continue
        fully_frgm_disk[free_i] = fully_frgm_disk[file_i]
        fully_frgm_disk[file_i] = '.'
        free_i += 1
        file_i -= 1

    print(sum(i * fully_frgm_disk[i] for i in range(len(fully_frgm_disk))
              if fully_frgm_disk[i] != '.'))

    smartly_frgm_disk = disk.copy()
    for file_i in range(len(smartly_frgm_disk) - 1, -1, -1):
        if file_i not in file_segments:
            continue
        file_size = file_segments[file_i]
        for free_i in range(file_i):
            if free_i not in free_spaces or free_spaces[free_i] < file_size:
                continue

            for i in range(file_size):
                smartly_frgm_disk[free_i + i] = smartly_frgm_disk[file_i + i]
                smartly_frgm_disk[file_i + i] = '.'

            old_free = free_spaces.pop(free_i)
            free_spaces[free_i + file_size] = old_free - file_size
            break

    print(sum(i * smartly_frgm_disk[i] for i in range(len(smartly_frgm_disk))
              if smartly_frgm_disk[i] != '.'))
