from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stack = []
        trapped = height[:]
        popElement = (0,0)

        for i, h in enumerate(height):
            while stack and h >= stack[-1][1]:
                popElement = stack.pop()
            if stack:
                left = stack[-1]
                for j in range(left[0] + 1, i):
                    trapped[j] = h
            else:
                left = popElement
                for j in range(left[0] +1, i):
                    trapped[j] = left[1]
            stack.append((i, h))

        for i in range(len(height)):
            diff = trapped[i] - height[i]
            answer += diff
        return answer



print(Solution.trap(Solution,[4,2,0,3,2,5]))

