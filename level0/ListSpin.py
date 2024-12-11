# https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=python3

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

print(solution([1, 2, 3], 'right'))
print(solution([1, 2, 3], 'left'))