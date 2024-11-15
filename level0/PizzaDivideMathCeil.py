import math


def solution(n):
    # 나머지가 있으면, 소수점이 있으니 그걸 올림하면 +1 되니까!
    return math.ceil(n / 7)

print(solution(1))
print(solution(2))
print(solution(7))
print(solution(24))

