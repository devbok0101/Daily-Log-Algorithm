from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def isValid(board, row, col):

            # 행 확인
            for i in range(n):
                if board[row][i] == 'Q':
                    return False

            # 열 확인
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # 왼쪽 대각선 확인
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # 오른쪽 대각선 확인
            i, j = row -1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -=1
                j += 1
            return True



        return []

print(Solution().solveNQueens(4))