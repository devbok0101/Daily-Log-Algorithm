from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## O(log n) 시간 복잡도로 풀기
        index = bisect_left(nums, target)

        if index != len(nums) and nums[index] == target:
            return index
        return -1

print(Solution.search(Solution, [-1,0,3,5,9,12], 9))