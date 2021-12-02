import re


cyclic_injection = '''
8: 42 | 42 8
11: 42 31 | 42 11 31'''


def rule_to_regex(num, rule):
    if rule == 'a' or rule == 'b':
        return rule
    regex = ['(?:']  # non-grouping

    rules_list = rule.split('|')
    for or_rule in rules_list:  # for all 'or options'
        and_rules = or_rule.split()
        for and_rule in and_rules:  # for all 'and elements'
            if num == and_rule:  # if rule is cyclic, ignore the cycle, but...
                continue
            regex.append(f'{{r{and_rule}}}')  # add format-able rule to regex

            if num in and_rules and and_rules[-1] == num:
                # if cyclic rule is at the end,
                regex.append('+')   # it just means repetition

        regex.append('|')  # add 'or' after each of the 'or options'

        # if cyclic rule is not at the end, it is in the middle  R: ab | aRb
        if num in and_rules and and_rules[-1] != num:
            and_rules.remove(num)  # remove it from the middle
            # and make options for 1 - 8 repetitions: ab|aabb|aaabbb|...
            for i in range(1, 8):
                regex.append('(?:')
                regex.append(f'{{r{and_rules[0]}}}' * i)
                regex.append(f'{{r{and_rules[1]}}}' * i)
                regex.append(')')
                regex.append('|')

    regex[-1] = ')'  # replace last '|' with the ')', finish group
    return ''.join(regex)


def refine_rules(rules_string):
    rules_dict = {}
    complete_rules = {}
    for line in rules_string.splitlines():
        num, rule = line.split(': ')

        rules_dict[num] = rule_to_regex(num, rule.strip('"'))

        if '{' not in rules_dict[num]:
            # no { mean there is no format-able rule placeholder
            complete_rules[f'r{num}'] = rules_dict[num]
        else:
            # otherwise, replace the format-able rule placeholder with itself
            complete_rules[f'r{num}'] = f'{{r{num}}}'

    # iteratively replace all the rules with complete rules
    clean = False
    while not clean:
        clean = True
        for num, rule in rules_dict.items():
            rules_dict[num] = rule.format(**complete_rules)
            if '{' not in rules_dict[num]:
                complete_rules[f'r{num}'] = rules_dict[num]
            else:
                # if at least one has {, then there is more to replace
                clean = False
    return complete_rules


if __name__ == '__main__':
    with open('src/day19.txt') as fp:
        inputs_ = fp.read()

    raw_rules, raw_messages = inputs_.split('\n\n')
    raw_rules_cyclic = raw_rules + cyclic_injection

    rules = refine_rules(raw_rules)
    rules_cyclic = refine_rules(raw_rules_cyclic)
    # rules now contain all rules as regexes
    main_regex = f'^{rules["r0"]}$'
    main_regex_cyclic = f'^{rules_cyclic["r0"]}$'
    # take the regex for 0, put it into ^$, and find the matches
    print(len(re.findall(main_regex, raw_messages, re.MULTILINE)))
    print(len(re.findall(main_regex_cyclic, raw_messages, re.MULTILINE)))
