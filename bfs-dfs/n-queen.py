def solve_queen(n):
    solutions = []
    board = [-1] * n

    def is_safe(row , col):
        for r in range(row):
            c = board[r]

            if c == col :
                return False
            if abs(c-col) == abs (r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(row , col):
                board[row] = col
                backtrack(row + 1 )
                board[row] = -1
    backtrack(0)
    return solutions

print(solve_queen(4))