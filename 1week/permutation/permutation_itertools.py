import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

print(Solution().permute([1,2,3]))