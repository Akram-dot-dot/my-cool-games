
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def bot_move(board):
    empty = get_empty_cells(board)
    return random.choice(empty)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    bot = "O"
    print_board(board)

    while True:
        if player == "X":
            row, col = map(int, input("Enter row and column (0-2): ").split())
        else:
            row, col = bot_move(board)
            print(f"Bot plays: {row}, {col}")

        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"{player} wins!")
            break

        if not get_empty_cells(board):
            print("It's a tie!")
            break

        player = bot if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
