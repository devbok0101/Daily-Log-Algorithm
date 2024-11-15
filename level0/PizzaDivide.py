def solution(n):
    answer = n // 7
    remain = n % 7

    if remain == 0:
        return answer

    if remain < 7:
        remain = 1

    return answer + remain

print(solution(1))
print(solution(2))
print(solution(7))
print(solution(24))

