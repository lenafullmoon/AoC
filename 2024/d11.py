
inputs_ = '''125 17'''


def find_final_expansion(stone, next_blink_of, depth, max_d):
    if depth == max_d:
        return len(next_blink_of[stone])
    length = 0
    for i in next_blink_of[stone]:
        length += find_final_expansion(i, next_blink_of, depth + 1, max_d)
    return length


if __name__ == '__main__':
    with open('inputs/d11.txt') as fp:
        inputs_ = fp.read()

    stones = [int(x) for x in inputs_.split()]
    next_blink_of = {}
    for a in range(75):
        swapstone = []
        for stone in stones:
            if stone in next_blink_of:
                # swapstone.extend(next_blink_of[stone])
                pass
            elif stone == 0:
                swapstone.append(1)
                next_blink_of[0] = [1]
            elif len(str(stone)) % 2 == 0:
                sstone = str(stone)
                half = len(sstone) // 2
                swapstone.append(int(sstone[:half]))
                swapstone.append(int(sstone[half:]))
                next_blink_of[stone] = [int(sstone[:half]), int(sstone[half:])]
            else:
                swapstone.append(stone * 2024)
                next_blink_of[stone] = [stone * 2024]
        stones = swapstone
    full_length = 0
    depth = 1
    # max_d = 75
    # precalc_lengths = {}
    # for stone, next_blink in next_blink_of.items():
    #     print(stone)
    #     precalc_lengths[stone] = []
    #     depth = 1
    #     for md in range(1, 25):
    #         precalc_lengths[stone].append(find_final_expansion(stone,
    #                                                            next_blink_of,
    #                                                            depth,
    #                                                            md,
    #                                                            precalc_lengths
    #                                                            ))
    #
    # print(precalc_lengths)
    for stone in [int(x) for x in inputs_.split()]:
        full_length += find_final_expansion(stone, next_blink_of, depth, 25)

    print(full_length)
