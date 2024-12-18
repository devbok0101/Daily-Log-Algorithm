# https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=python3
from collections import deque


# 시간복잡도 기준으로 insert(0, ...)는 O(n)이므로 비효율적
def solution(numbers, direction):
    if direction == 'left':
        first_num = numbers[0]
        numbers = numbers[1:]
        numbers.append(first_num)
        return numbers

    if direction == 'right':
        last_num = numbers[len(numbers) - 1]
        numbers = numbers[:len(numbers) - 1]
        numbers.insert(0, last_num)
        return numbers

# 시간복잡도 기준으로 deque를 양쪽 끝에서 삽입 삭제가 O(1)이므로 효율적
def solution2(numbers, direction):
    numbers_que = deque(numbers)

    if direction == "right":
        numbers_que.rotate(1)
    if direction == "left":
        numbers_que.rotate(-1)

    return list(numbers_que)

print(solution2([1, 2, 3], 'right'))
print(solution2([1, 2, 3], 'left'))