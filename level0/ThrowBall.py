# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    numbers = numbers * k

    count = 0
    throw = 2
    answer = 0
    while count <= k:
        count += 1
        if count == k:
            break
        answer = numbers[0 + throw]
        throw += 2

    return answer

def solution2(numbers, k):
    return numbers[(2 * (k - 1)) % len(numbers)]

print(solution2([1, 2, 3, 4], 2))
print(solution2([1, 2, 3, 4, 5, 6], 5))
print(solution2([1, 2, 3], 3))