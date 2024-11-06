from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max <= right_max:
                left += 1
                if height[left] < left_max:
                    answer += left_max - height[left]
                else:
                    left_max = height[left]
            else:
                right -= 1
                if height[right] < right_max:
                    answer += right_max - height[right]
                else:
                    right_max = height[right]
        return answer



print(Solution.trap(Solution,[0,1,0,2,1,0,1,3,2,1,2,1]))

