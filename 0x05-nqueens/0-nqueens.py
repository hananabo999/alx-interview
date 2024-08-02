#!/usr/bin/python3
"""Module for N queens problem."""


def queen(N):
    output = []
    pos = []

    def helper_function(x: int):
        if x == N:
            output.append(pos[:])
            return

        for y in range(N):
            if is_valid(pos, x, y):
                pos.append([x, y])
                helper_function(x + 1)
                pos.pop()  # Backtrack

    def is_valid(board, x, y):
        for row in board:
            if (x == row[0] or y == row[1] or x + y == row[0] + row[1] or
                    x - y == row[0] - row[1]):
                return False
        return True

    helper_function(0)
    return output


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = queen(N)
    for solution in solutions:
        print(solution)
