from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = defaultdict(list)

        for index, num in enumerate(nums):
            ans[num].append(index)

        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [ans[nums[left]][0], ans[nums[right]][-1]]


#print(Solution.twoSum(Solution,[2,7,11,15], 9))
#print(Solution.twoSum(Solution,[3,2,4], 6))
(Solution.twoSum(Solution,[3,3], 6))