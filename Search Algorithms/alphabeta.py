def alphabeta(game, depth, alpha, beta, maximizing):
    # Terminal states
    winner = game.winner()

    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if game.is_full():
        return 0

    # Maximizing player (X)
    if maximizing:
        value = -float("inf")

        for move in game.available_moves():
            game.make_move(move, 'X')

            value = max(
                value,
                alphabeta(game, depth + 1, alpha, beta, False)
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
                alphabeta(game, depth + 1, alpha, beta, True)
            )

            game.undo_move(move)

            beta = min(beta, value)

            # Prune branch
            if beta <= alpha:
                break

        return value


def best_move_ab(game):
    best_score = -float("inf")
    best_move = None

    for move in game.available_moves():
        game.make_move(move, 'X')

        score = alphabeta(
            game,
            0,
            -float("inf"),
            float("inf"),
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move