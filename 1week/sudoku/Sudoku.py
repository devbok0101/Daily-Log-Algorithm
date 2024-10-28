class Solution:
    def solveSudoku(self, board):

        def check_empty(board, row, column):
            if board[row][column] != ".":
                return False
            return True

        def check_valid(board, num, row, column):

            for i in range(9):

                if board[row][i] == num:
                    return False
                if board[i][column] == num:
                    return False
                if board[(row // 3) * 3 + i // 3][(column // 3) * 3 + i % 3] == num:
                    return False

            return True

        def backTrack(board, index):

            if index == 81:
                return True

            i, j = index // 9, index % 9

            if check_empty(board, i, j):
                for num in map(str, range(1, 10)):
                    if check_valid(board, num, i, j):
                        board[i][j] = num
                        if backTrack(board, index + 1):
                            return True
                        board[i][j] = "."
            else:
                backTrack(board, index + 1)

        backTrack(board, 0)
