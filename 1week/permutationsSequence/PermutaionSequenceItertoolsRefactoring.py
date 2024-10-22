import itertools
from collections import defaultdict
from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial= [i+1 for i in range(n)]
        return "".join(map(str, list(permutations(factorial, n))[k-1]))


print(Solution().getPermutation(4, 9))