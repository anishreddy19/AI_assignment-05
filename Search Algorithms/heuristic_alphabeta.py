def heuristic(game):
    # Evaluate board position
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    score = 0

    for line in lines:
        values = [game.board[i] for i in line]

        if values.count('X') == 2 and values.count(' ') == 1:
            score += 10

        if values.count('O') == 2 and values.count(' ') == 1:
            score -= 10

        if values.count('X') == 1 and values.count(' ') == 2:
            score += 1

        if values.count('O') == 1 and values.count(' ') == 2:
            score -= 1

    return score


def heuristic_ab(game, depth, alpha, beta, maximizing, limit):
    # Terminal states
    winner = game.winner()

    if winner == 'X':
        return 100

    if winner == 'O':
        return -100

    if game.is_full():
        return 0

    # Depth cutoff
    if depth == limit:
        return heuristic(game)

    # Maximizing player (X)
    if maximizing:
        value = -float("inf")

        for move in game.available_moves():
            game.make_move(move, 'X')

            value = max(
                value,
                heuristic_ab(
                    game,
                    depth + 1,
                    alpha,
                    beta,
                    False,
                    limit
                )
            )

            game.undo_move(move)

            alpha = max(alpha, value)

            # Prune branch
            if alpha >= beta:
                break

        return value

    # Minimizing player (O)
    else:
        value = float("inf")

        for move in game.available_moves():
            game.make_move(move, 'O')

            value = min(
                value,
                heuristic_ab(
                    game,
                    depth + 1,
                    alpha,
                    beta,
                    True,
                    limit
                )
            )

            game.undo_move(move)

            beta = min(beta, value)

            # Prune branch
            if beta <= alpha:
                break

        return value


def best_move_hab(game, limit=3):
    best_score = -float("inf")
    best_move = None

    for move in game.available_moves():
        game.make_move(move, 'X')

        score = heuristic_ab(
            game,
            0,
            -float("inf"),
            float("inf"),
            False,
            limit
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move