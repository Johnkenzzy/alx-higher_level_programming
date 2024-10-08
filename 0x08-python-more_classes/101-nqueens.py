#!/usr/bin/python3
"""
Thsi is module 101-nqueens

This provides a program that solves the N queens problem
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""
    for i in range(row):
        if board[i] == col:
            return (False)

    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return (False)

    return (True)


def solve_nqueens(N, row, board, solutions):
    """Use backtracking to solve the N Queens problem."""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)


def nqueens(N):
    """Main function to solve the N Queens problem."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
