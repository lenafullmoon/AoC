def calc_score(winner):
    _, winner = winner
    return sum(c * (len(winner) - i) for i, c in enumerate(winner))


def parse_input_decks(inputs):
    inputs = inputs.splitlines()
    index_player2 = inputs.index('Player 2:')
    player1 = [int(x) for x in inputs[1:index_player2 - 1]]
    player2 = [int(x) for x in inputs[index_player2 + 1:]]
    return player1, player2


def win_round(player1, player2, c1, c2, winner):
    if winner == 1:
        player1.append(c1)
        player1.append(c2)
    if winner == 2:
        player2.append(c2)
        player2.append(c1)


def combat(player1, player2):
    while True:
        c1 = player1.pop(0)
        c2 = player2.pop(0)

        wins = 1 if c1 > c2 else 2
        win_round(player1, player2, c1, c2, wins)

        if len(player1) == 0:
            return 2, player2
        if len(player2) == 0:
            return 1, player1


def hash_game(player1, player2):
    return f'{calc_score((0, player1))}:{calc_score((0, player2))}'


def recursive_combat(player1, player2):
    games = set()
    while True:
        game_hash = hash_game(player1, player2)
        if game_hash in games:
            return 1, player1
        games.add(game_hash)

        c1 = player1.pop(0)
        c2 = player2.pop(0)
        if c1 > len(player1) or c2 > len(player2):
            wins = 1 if c1 > c2 else 2
        else:
            wins, _ = recursive_combat(player1.copy()[:c1],
                                       player2.copy()[:c2])
        win_round(player1, player2, c1, c2, wins)

        if len(player1) == 0:
            return 2, player2
        if len(player2) == 0:
            return 1, player1


if __name__ == '__main__':
    with open('src/day22.txt') as fp:
        inputs_ = fp.read()
    print(calc_score(combat(*parse_input_decks(inputs_))))
    print(calc_score(recursive_combat(*parse_input_decks(inputs_))))
