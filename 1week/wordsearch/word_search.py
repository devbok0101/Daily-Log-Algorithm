from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m= len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]

        def in_range(i, j):
            if 0 <= i < n and 0 <= j < m:
                return True
            return False

        def backTracking(i, j, w, visited):
            if not visited[i][j] and board[i][j] == word[w]:
                if w == len(word) -1:
                    return True

                visited[i][j] = True
                flag = False

                for x, y in [[0,1], [1,0], [-1,0], [0, -1]]:
                    if in_range(x + i, y + j):
                        if backTracking(x + i, y + j, w + 1, visited):
                            flag = True
                visited[i][j] = False
                return flag

        for i in range(n):
            for j in range(m):
                backTracking(i, j, 0, visited)
                return True

            return False


print(Solution.exist(Solution, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))