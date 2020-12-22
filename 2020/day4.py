import re
BY, IY, EY, HT, HC, EC, PID = 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
MANDATORY_KEYS = {BY, IY, EY, HT, HC, EC, PID}

OPT_KEYS = {'cid'}


def parse_line(line):
    result = {}
    key_values = line.split()
    for kv in key_values:
        k, v = kv.split(':')
        result[k] = v
    return result


def is_hex(string):
    if re.match('[0-9a-fA-F]{6}', string):
        return True
    return False


def is_valid(pp):
    if not (pp[BY].isdigit() and pp[IY].isdigit()
            and pp[EY].isdigit() and pp[PID].isdigit()):
        return False

    if int(pp[BY]) < 1920 or int(pp[BY]) > 2002:
        return False
    if int(pp[IY]) < 2010 or int(pp[IY]) > 2020:
        return False
    if int(pp[EY]) < 2020 or int(pp[EY]) > 2030:
        return False

    if len(pp[PID]) != 9:
        return False

    if pp[EC] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if not (pp[HC].startswith('#') and len(pp[HC]) == 7
            and is_hex(pp[HC][1:])):
        return False

    if not pp[HT].endswith('cm') and not pp[HT].endswith('in'):
        return False
    if pp[HT].endswith('cm'):
        h = int(pp[HT][:-2])
        if h < 150 or h > 193:
            return False
    if pp[HT].endswith('in'):
        h = int(pp[HT][:-2])
        if h < 59 or h > 76:
            return False
    return True


if __name__ == '__main__':
    with open('src/day4.txt') as fp:
        lines = [line.strip() for line in fp.readlines()]

        valid_counter = 0
        content = {}

        for line in lines:
            if line == '':
                if MANDATORY_KEYS <= content.keys() and is_valid(content):
                    valid_counter += 1
                content = {}
            else:
                content.update(**parse_line(line))

        print(valid_counter)
