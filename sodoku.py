
import random
import time

step = 0


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


def show(board, title):
    print("\n" + "=" * 35)
    print(title)
    print("=" * 35)

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


def generate(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)

                for num in nums:
                    if valid(board, row, col, num):
                        board[row][col] = num

                        if generate(board):
                            return True

                        board[row][col] = 0

                return False

    return True


def solve(board):
    global step

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if valid(board, row, col, num):
                        board[row][col] = num
                        step += 1

                        show(board, f"Step {step}: Place {num} at ({row+1}, {col+1})")
                        time.sleep(0.2)

                        if solve(board):
                            return True

                        board[row][col] = 0
                        step += 1

                        show(board, f"Step {step}: Backtracking at ({row+1}, {col+1})")
                        time.sleep(0.2)

                return False

    return True


# Generate random Sudoku
board = [[0] * 9 for _ in range(9)]
generate(board)

# Remove 40 numbers
cells = [(r, c) for r in range(9) for c in range(9)]
random.shuffle(cells)

for r, c in cells[:40]:
    board[r][c] = 0

# Start solving
show(board, "Initial Sudoku")

input("\nPress Enter to start...")

solve(board)

show(board, "Sudoku Completed!")
print("\nCongratulations! Puzzle Solved.")
