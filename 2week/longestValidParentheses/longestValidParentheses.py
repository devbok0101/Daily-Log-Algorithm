from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        array = [0] * n

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')' and stack:
                match_position = stack.pop()
                array[match_position] = 1
                array[i] = 1

        max_len = 0
        current_len = 0

        for num in array:
            if num == 1:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0

        return max_len

print(Solution.longestValidParentheses(Solution, "()()())()()"))
