from collections import deque


def solution(queue1, queue2):
    queue = queue1 + queue2

    q1_sum = sum(queue1)
    target = (sum(queue1) + sum(queue2)) // 2

    left, right = 0, len(queue1)

    for answer in range(0, len(queue1) * 3):
        if q1_sum > target:
            q1_sum -= queue[left]
            left = (left + 1) % len(queue)
        elif target > q1_sum:
            q1_sum += queue[right]
            right = (right + 1) % len(queue)
        else:
            return answer

    return -1


#print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
#print(solution([1], [1]))
