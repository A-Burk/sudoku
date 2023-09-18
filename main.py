import time

# Print current state of puzzle
def print_puzzle(puzzle):
    for i in range(9):
        print(puzzle[i])
        # for j in range(9):
        #     print(puzzle[i][j])
        #     if (j == 2) or (j == 5):
        #         print('\t\t')

    print()


# Find an empty spot in the puzzle
def find_blank(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j

    return None, None


# Verify that a guess does not violate any rules
def check_guess(puzzle, row, col, guess):
    if guess in puzzle[row]:
        return False

    for i in range(9):
        if puzzle[i][col] == guess:
            return False

    square_x = (col // 3) * 3
    square_y = (row // 3) * 3
    for i in range(square_y, square_y + 3):
        for j in range(square_x, square_x + 3):
            if puzzle[i][j] == guess:
                return False

    return True


# Recursively find blanks, make guesses, and backtrack as necessary
def solve_puzzle(puzzle):
    row, col = find_blank(puzzle)

    if row is None:
        print_puzzle(puzzle)
        return True

    for i in range(1, 10):
        if check_guess(puzzle, row, col, i):
            puzzle[row][col] = i
            if solve_puzzle(puzzle):
                return True

        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    puzzle_blank = [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],

        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],

        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]
    puzzle_easy = [
        [-1, -1, 6, -1, -1, -1, 5, -1, 8],
        [1, -1, 2, 3, 8, -1, -1, -1, 4],
        [-1, -1, -1, 2, -1, -1, 1, 9, -1],

        [-1, -1, -1, -1, 6, 3, -1, 4, 5],
        [-1, 6, 3, 4, -1, 5, 8, 7, -1],
        [5, 4, -1, 9, 2, -1, -1, -1, -1],

        [-1, 8, 7, -1, -1, 4, -1, -1, -1],
        [2, -1, -1, -1, 9, 8, 4, -1, 7],
        [4, -1, 9, -1, -1, -1, 3, -1, -1]
    ]
    puzzle_unsolvable = [
        [1, 2, 3, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 4, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 1],

        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]
    puzzle_advanced = [
        [-1, 9, -1, -1, -1, -1, 8, 3, -1],
        [-1, -1, 3, 6, -1, -1, -1, 4, -1],
        [-1, -1, 8, -1, -1, -1, -1, -1, -1],

        [2, -1, -1, -1, 9, -1, -1, -1, -1],
        [-1, -1, -1, 4, 3, 8, -1, -1, -1],
        [9, -1, 5, -1, 6, -1, -1, -1, -1],

        [-1, -1, -1, 7, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, -1, 4, -1, -1, 6],
        [1, 7, -1, -1, -1, -1, -1, -1, 5],
    ]

    number_choice = input("Pick a number between 1 and 4\n")
    print()
    puzzle_choice = puzzle_easy
    match number_choice:
        case "1":
            print("You chose the blank puzzle\n")
            puzzle_choice = puzzle_blank
        case "2":
            print("You chose the easy puzzle\n")
            puzzle_choice = puzzle_easy
        case "3":
            print("You chose the unsolvable puzzle\n")
            puzzle_choice = puzzle_unsolvable
        case "4":
            print("You chose the advanced puzzle\n")
            puzzle_choice = puzzle_advanced
        case _:
            print("Invalid input, solving the easy puzzle\n")

    print_puzzle(puzzle_choice)

    tic = time.perf_counter()

    if not(solve_puzzle(puzzle_choice)):
        print("Not solvable")

    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
