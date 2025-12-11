def has_same_segments(phrase, segment_len):
    if len(phrase) % segment_len != 0:
        return False
    first_segment = phrase[:segment_len]
    for i in range(1, len(phrase) // segment_len):
        seg_start = i * segment_len
        if phrase[seg_start:seg_start + segment_len] != first_segment:
            return False
    return True


if __name__ == '__main__':
    with open('inputs/d02.txt') as fp:
        inputs_ = fp.read()
    sum_of_invalid_ids_simple = 0
    sum_of_invalid_ids = 0
    for id_range in inputs_.split(','):
        start, end = id_range.split('-')
        for x in range(int(start), int(end) + 1):
            sx = str(x)
            lx = len(sx)

            if lx % 2 == 0 and has_same_segments(sx, lx // 2):
                sum_of_invalid_ids_simple += x
            for seg_len in range(1, lx // 2 + 1):
                if has_same_segments(sx, seg_len):
                    sum_of_invalid_ids += x
                    break

    print(sum_of_invalid_ids_simple)
    print(sum_of_invalid_ids)


