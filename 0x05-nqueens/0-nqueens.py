#!/usr/bin/python3
"""doc doc doc"""
import sys
from typing import List


def solve_queens_problem(board_size: int) -> List[List[int]]:
    """doc doc doc"""

    def is_valid_position(pos: int, occupied_pos: List[int]) -> bool:
        """doc doc doc"""
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos
                or occupied_pos[i] - i == pos - len(occupied_pos)
                or occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(
        board_size: int, index: int, occupied_pos: List[int],
        solutions: List[List[int]]
    ) -> None:
        """doc doc doc"""
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions: List[List[int]] = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main() -> None:
    """doc doc doc"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
