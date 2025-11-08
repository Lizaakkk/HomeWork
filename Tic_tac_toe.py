def print_board(board):
    print("\n    | 0 | 1 | 2 |")
    print("------------------")
    for i in range(3):
        row_display = [cell if cell != '-' else ' ' for cell in board[i]]
        print(f"  {i} | {' | '.join(row_display)} |")
        print("------------------")


def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != '-':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True


def make_move(board, row, col, player):
    if board[row][col] == '-':
        board[row][col] = player
        return True
    return False


def tic_tac_toe():
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    current_player = 'X'

    print("Добро пожаловать в Крестики-нолики!")
    print("Игроки по очереди вводят координаты хода (строка столбец)")
    print("Например: '0 1' для первой строки и второго столбца\n")

    while True:
        print_board(board)

        try:
            move = input(f"Ход игрока {current_player} (строка столбец): ").split()
            if len(move) != 2:
                print("Введите две координаты через пробел!")
                continue

            row, col = int(move[0]), int(move[1])

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Координаты должны быть от 0 до 2!")
                continue

            if not make_move(board, row, col, current_player):
                print("Эта клетка уже занята!")
                continue

        except (ValueError, IndexError):
            print("Некорректный ввод! Используйте формат: '0 1'")
            continue
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Поздравляем! Игрок {winner} победил!")
            break
        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    tic_tac_toe()