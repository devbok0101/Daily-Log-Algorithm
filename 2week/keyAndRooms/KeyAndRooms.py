from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [False] * len(rooms)

        def dfs(v):
            visited[v] = True
            for next_v in rooms[v]:
                if not visited[next_v]:
                    dfs(next_v)

        dfs(0)

        return all(visited)


print(Solution.canVisitAllRooms(Solution, [[1], [2], [3], []]))
