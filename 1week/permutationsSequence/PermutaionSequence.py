import itertools
from collections import defaultdict


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        ans = itertools.permutations(range(1, n + 1), n)

        for index, value in enumerate (ans):
            if index == k - 1:
                return ''.join(map(str, value))


        return ''


print(Solution().getPermutation(4, 9))