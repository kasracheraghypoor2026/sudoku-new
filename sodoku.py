
import random
import time

step = 0


# Check Sudoku rules
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


# Display Sudoku
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


# Generate a complete Sudoku
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


# Backtracking solver for computer mode
def solve(board):
    global step

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if valid(board, row, col, num):
                        board[row][col] = num
                        step += 1

                        show(board, f"Step {step}: Place {num}")
                        time.sleep(0.2)

                        if solve(board):
                            return True

                        board[row][col] = 0
                        step += 1

                        show(board, f"Step {step}: Backtracking")
                        time.sleep(0.2)

                return False

    return True


# Check whether the player's move allows a solution
def check_solution(board, stats, trace):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if valid(board, row, col, num):

                        board[row][col] = num
                        stats["tries"] += 1

                        trace.append(f"TRY: {num} at ({row+1},{col+1})")

                        if check_solution(board, stats, trace):
                            return True

                        board[row][col] = 0
                        stats["backtracks"] += 1

                        trace.append(
                            f"BACKTRACK: Remove {num} from ({row+1},{col+1})"
                        )

                return False

    return True


# Player mode with Backtracking
def player(board, solution):

    while True:
        show(board, "Player Mode")

        if board == solution:
            print("\nCongratulations! You Won!")
            break

        try:
            row = int(input("\nEnter row (1-9) or 0 to exit: "))

            if row == 0:
                break

            col = int(input("Enter column (1-9): "))
            num = int(input("Enter number (1-9): "))

            if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                print("Invalid input!")
                continue

            row -= 1
            col -= 1

            if board[row][col] != 0:
                print("This cell is already filled!")
                continue

            if not valid(board, row, col, num):
                print("Invalid move! Number already exists.")
                continue

            # Temporarily place player's number
            board[row][col] = num

            # Make a copy for Backtracking
            test_board = [r[:] for r in board]

            stats = {"tries": 0, "backtracks": 0}
            trace = []

            print("\nChecking your move with Backtracking...")

            possible = check_solution(test_board, stats, trace)

            print("\n===== Backtracking Report =====")
            print("Number of attempts:", stats["tries"])
            print("Number of backtracks:", stats["backtracks"])

            for event in trace[-8:]:
                print(event)

            if possible:
                print("\nMove Accepted! The puzzle is solvable.")
            else:
                board[row][col] = 0
                print("\nDead End! Backtracking rejected your move.")
                print("Try another number.")

        except ValueError:
            print("Please enter numbers only!")


# Create Sudoku
board = [[0] * 9 for _ in range(9)]

generate(board)

# Save complete solution
solution = [row[:] for row in board]

# Remove 40 numbers
cells = [(r, c) for r in range(9) for c in range(9)]
random.shuffle(cells)

for r, c in cells[:40]:
    board[r][c] = 0

# Game menu
print("\n===== SUDOKU GAME =====")
print("1. Computer Solve")
print("2. Player Mode with Backtracking")

choice = input("\nChoose mode (1 or 2): ")

if choice == "1":

    show(board, "Initial Sudoku")
    input("\nPress Enter to start...")

    solve(board)

    show(board, "Sudoku Completed!")
    print("\nComputer Solved the Puzzle!")

elif choice == "2":

    player(board, solution)

else:
    print("Invalid choice!")

