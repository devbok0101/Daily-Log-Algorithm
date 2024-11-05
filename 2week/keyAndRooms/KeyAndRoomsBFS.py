from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [False] * len(rooms)

        def bfs(v):
            queue = deque()
            queue.append(v)

            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        queue.append(next_v)
                        visited[next_v] = True


        bfs(0)

        return all(visited)


print(Solution.canVisitAllRooms(Solution, [[1, 3], [3, 0, 1], [2], [0]]))
