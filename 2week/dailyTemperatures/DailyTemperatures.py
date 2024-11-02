from collections import defaultdict
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        start, last = 0, len(temperatures)
        answer = [0 for _ in range(last)]

        stack = []
        while last - 1 >= start:
            stack.append(temperatures[last - 1])
            last -= 1

        for index in range(len(temperatures)):
            nowTemp = temperatures[index]
            for i in range(index + 1):
                stack.pop()
            nextTemp = stack[0]




        return answer


print(Solution.dailyTemperatures(Solution, [73,74,75,71,69,72,76,73]))