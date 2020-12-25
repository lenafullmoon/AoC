def transform(subject_number, loop_size):
    return subject_number ** loop_size % 20201227


def find_loop_size(public_key1, public_key2):
    value = 1
    subject_number = 7
    loop_size = 0
    ls1, ls2 = None, None
    while not ls1 or not ls2:
        value *= subject_number
        remainder = value % 20201227
        loop_size += 1
        if remainder == public_key1:
            ls1 = loop_size
            break
        if remainder == public_key2:
            ls2 = loop_size
            break
    return ls1, ls2


if __name__ == '__main__':
    card_pub = 2084668
    door_pub = 3704642

    card_loop, door_loop = find_loop_size(card_pub, door_pub)
    print(card_loop, door_loop)
    if card_loop:
        print(transform(door_pub, card_loop))
    if door_loop:
        print(transform(card_pub, door_loop))

# this was done bruteforce
# #(T=3164.507903814316) find_loop_size
# None 2115361
