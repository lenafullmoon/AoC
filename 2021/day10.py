rules = {
    ')': {'score1': 3, 'score2': 1, 'open': '('},
    ']': {'score1': 57, 'score2': 2, 'open': '['},
    '}': {'score1': 1197, 'score2': 3, 'open': '{'},
    '>': {'score1': 25137, 'score2': 4, 'open': '<'}
}
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

if __name__ == '__main__':
    with open('src/day10.txt') as fp:
        inputs_ = fp.read()
    score1 = 0
    score2 = []
    for line in inputs_.splitlines():
        stack = []
        for c in line:
            if c in pairs:
                stack.append(c)
            elif rules[c]['open'] == stack[-1]:
                stack.pop()
            else:
                score1 += rules[c]['score1']
                break
        else:  # done with corrupt lines, onto incomplete lines
            score = 0
            for c in stack[::-1]:
                score = score * 5 + rules[pairs[c]]['score2']
            score2.append(score)
    print(score1)
    print(sorted(score2)[int(len(score2)/2)])
