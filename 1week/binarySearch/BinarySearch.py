from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## O(log n) 시간 복잡도로 풀기

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

print(Solution.search(Solution, [-1,0,3,5,9,12], 9))