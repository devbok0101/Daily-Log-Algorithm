from collections import deque


def solution(queue1, queue2):
    answer = -1
    qsize = len(queue1)

    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)

    for i in range(0, qsize*3):
        if q1_sum == q2_sum:
            return i
        elif q1_sum < q2_sum:
            num1 = q2.popleft()
            q1.append(num1)
            q1_sum += num1
            q2_sum -= num1
        elif q1_sum > q2_sum:
            num2 = q1.popleft()
            q2.append(num2)
            q1_sum -= num2
            q2_sum += num2

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
#print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1], [1]))
