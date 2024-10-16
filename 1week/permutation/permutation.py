from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backTrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backTrack(curr)
                    curr.pop()

        ans = []
        backTrack([])
        return ans

print(Solution().permute([1,2,3]))