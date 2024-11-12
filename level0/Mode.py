from collections import defaultdict


def solution(array):

    answer = defaultdict(list)
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if array[i] not in answer[count]:
            answer[count].append(array[i])
        count = 0

    index = max(answer)

    if len(answer[index]) > 1:
        return -1

    return answer[index][0]

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([8,8,8,8,8]))