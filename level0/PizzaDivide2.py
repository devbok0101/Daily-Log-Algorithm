def solution(n):
    answer = 1

    while (6 * answer) % n != 0:
        answer += 1

    return answer


print(solution(6))
print(solution(10))
print(solution(4))
print(solution(1))