MY_BAG = 'shiny gold'
NO_BAGS = 'no other bags'


def parse_rule(line):
    bag, content = line.split(' bags contain ')
    if content.startswith(NO_BAGS):
        return bag, {}
    content = content.strip('.').split(',')
    rule = {}
    for bags in content:
        words = bags.split()
        amount = int(words[0])
        ibag = words[1] + ' ' + words[2]
        rule[ibag] = amount
    return bag, rule


def gather_rules(lines):
    rules = {}
    for line in lines:
        bag, rule = parse_rule(line)
        rules[bag] = rule
    return rules


def all_containers(bag, rules):
    containers = set()
    for dir_bag, rule in rules.items():
        if bag in rule:
            containers.add(dir_bag)
            containers |= all_containers(dir_bag, rules)
    return containers


def count_inners(bag, rules):
    count = 0
    for k, v in rules[bag].items():
        count += v + v * count_inners(k, rules)
    return count


def containers_iter(rules):
    def find_all_containers(bag, rules):
        dir_containers = set()
        for dir_bag, rule in rules.items():
            if bag in rule:
                dir_containers.add(dir_bag)
        return dir_containers
    unprocessed = {MY_BAG}
    containers = set()
    while True:
        level_conts = set()
        for unp in unprocessed:
            level_conts |= find_all_containers(unp, rules)
        containers |= level_conts
        unprocessed = level_conts
        if level_conts == set():
            break
    print(len(containers))


if __name__ == '__main__':
    with open('src/day7.txt') as fp:
        rulz = gather_rules([line.strip() for line in fp.readlines()])

        containers_iter(rulz)
        print(len(all_containers(MY_BAG, rulz)))
        print(count_inners(MY_BAG, rulz))
