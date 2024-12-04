#https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i : i + n])

    return answer


def solution2(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i : i + n])

    return [num_list[i : i + n] for i in range(0, len(num_list), n)]


print(solution2([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution2([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))