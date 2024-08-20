def find_winner(board):
    n = len(board)
    start_dir = [(r, 0, 0, 1) for r in range(n)]
    start_dir.extend([0, c, 1, 0] for c in range(n))
    start_dir.append((0, 0, 1, 1))
    start_dir.append((0, n-1, 1, -1))

    for r, c, dr, dc in start_dir:
        player = board[r][c]
        if player == ' ':
            continue
        is_win = True
        for s in range(n):
            if board[r][c] != player:
                is_win = False
                break
            r, c = r + dr, c + dc
        if is_win:
            return player
    return None


if __name__ == '__main__':
    n = int(input('Enter grid size: '))
    assert n >= 3
    board = [[' ']*n for i in range(n)]
    symbols = 'XO'
    steps, turn = 0, 0

    while True:
        if steps == n * n:
            print('Tie!')
            break
        r, c = map(int, input(f'player {symbols[turn]}, make a move: ').split())
        r, c = r-1, c-1
        if not 0 <= r < n or not 0 <= c < n or board[r][c] != ' ':
            print('Invalid location. Try again')
            continue
        board[r][c] = symbols[turn]
        print('\n'.join(['|'.join(row) for row in board]))

        if (winner := find_winner(board)) is not None:
            print(f'play {winner} won!')
            break
        turn = 1-turn
