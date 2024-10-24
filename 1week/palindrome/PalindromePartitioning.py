from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        result = []

        def back_track(start, partition):
            if len(s) == start:
                result.append(partition[:])
                return

            for i in range(start + 1, len(s) + 1):
                slicing = s[start:i]
                if slicing == slicing[::-1]:
                    partition.append(slicing)
                    back_track(i, partition)
                    partition.pop()

        back_track(0, [])
        return result


print(Solution.partition(Solution, "aab"))
