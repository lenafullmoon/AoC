# 28901 too low
import re
inputs_ = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

# inputs_ = '''Button A: X+30, Y+30
# Button B: X+30, Y+30
# Prize: X=60, Y=60'''


class Position:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Position(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return Position(self.i - other.i, self.j - other.j)

    def __repr__(self):
        return f'({self.i}, {self.j})'

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash((self.i, self.j))


class ClawMachine:
    def __init__(self, a: Position, b: Position, prize: Position):
        self.button_a = a
        self.button_b = b
        self.prize = prize

    @classmethod
    def from_lines(cls, lines):
        coordinate = re.compile(r'(\d+)')
        a = Position(*[int(x) for x in coordinate.findall(lines[0])])
        b = Position(*[int(x) for x in coordinate.findall(lines[1])])
        prize = Position(*[int(x) for x in coordinate.findall(lines[2])])
        return ClawMachine(a, b, prize)

    def __repr__(self):
        return f'<{self.prize} ({self.button_a}, {self.button_b})>'


if __name__ == '__main__':
    with open('inputs/d13.txt') as fp:
        inputs_ = fp.read()
    lines = inputs_.splitlines(keepends=False)
    machines = [ClawMachine.from_lines(lines[i:i+4])
                for i in range(0, len(lines), 4)]

    tokens_spent = 0
    for m in machines:
        possible_repetitions = []
        for x_a in range(m.prize.i // m.button_a.i + 1):
            by_a = x_a * m.button_a.i
            x_b = (m.prize.i - by_a) // m.button_b.i
            if x_a * m.button_a.i + x_b * m.button_b.i == m.prize.i:
                possible_repetitions.append((x_a, x_b))
        confirmed_repetitions = []
        for y_a in range(m.prize.j // m.button_a.j + 1):
            by_a = y_a * m.button_a.j
            y_b = (m.prize.j - by_a) // m.button_b.j
            if y_a * m.button_a.j + y_b * m.button_b.j== m.prize.j:
                if (y_a, y_b) in possible_repetitions:
                    confirmed_repetitions.append((y_a, y_b))

        if len(confirmed_repetitions) == 1:
            single_solution = confirmed_repetitions[0]
            tokens_spent += single_solution[0] * 3 + single_solution[1]
        elif len(confirmed_repetitions) != 0:
            print('Well this is gonna be a problem...')
    print(tokens_spent)
