from collections import defaultdict
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day = stack.pop()[0]
                answer[prev_day] = day - prev_day
            stack.append((day, temp))

        return answer


print(Solution.dailyTemperatures(Solution, [73,74,75,71,69,72,76,73]))