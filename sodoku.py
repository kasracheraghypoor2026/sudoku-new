
import random
import time

def valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    sr = (row // 3) * 3
    sc = (col // 3) * 3

    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for num in numbers:
                    if valid(board, row, col, num):
                        board[row][col] = num

                        time.sleep(0.03)
                        show(board)

                        if solve(board):
                            return True

                        board[row][col] = 0
                        show(board)

                return False

    return True


def show(board):
    print("\033[H\033[J", end="")

    for i in range(9):
        if i % 3 == 0:
            print("+-------+-------+-------+")

        print("|", end=" ")

        for j in range(9):
            print(board[i][j] if board[i][j] else ".", end=" ")

            if j % 3 == 2:
                print("|", end=" ")

        print()

    print("+-------+-------+-------+")


# ساخت جدول تصادفی کامل
board = [[0] * 9 for _ in range(9)]
solve(board)

# خالی کردن ۴۰ خانه
cells = [(r, c) for r in range(9) for c in range(9)]
random.shuffle(cells)

for r, c in cells[:40]:
    board[r][c] = 0

print("Initial Sudoku:")
show(board)

input("Press Enter to start automatic solving...")

print("Solving Sudoku...")
solve(board)

print("Sudoku Solved!")
show(board)
