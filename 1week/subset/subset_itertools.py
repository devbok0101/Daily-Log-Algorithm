import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(nums) + 1):
            ans.extend(itertools.combinations(nums, i))
        return ans


print(Solution().subsets([1, 2, 3]))