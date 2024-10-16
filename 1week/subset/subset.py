import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backTrack(start, path):
            ans.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backTrack(i + 1, path)
                path.pop()


        ans = []
        backTrack(0, [])
        return ans


print(Solution().subsets([1, 2, 3]))