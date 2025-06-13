
def mini_chess_challenge():
    board = [[" "]*8 for _ in range(8)]
    board[6][3] = "P"  # Pawn
    board[1][3] = "K"  # Target king position

    def print_board():
        for row in board:
            print(" ".join(row))
        print()

    def move_pawn():
        x, y = 6, 3
        while x > 0:
            board[x][y] = " "
            x -= 1
            board[x][y] = "P"
            print_board()
            if x == 1:
                print("Pawn reached the enemy King!")
                break
            input("Press Enter for next move...")

    print_board()
    move_pawn()

if __name__ == "__main__":
    mini_chess_challenge()
