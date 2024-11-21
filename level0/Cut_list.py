# https://school.programmers.co.kr/learn/courses/30/lessons/120833

def solution(numbers, num1, num2):
    answer = []

    for index, num in enumerate(numbers):
        if index == num1 and index <= num2:
            answer.append(num)
            num1 += 1


    return answer


print(solution([1, 2, 3, 4, 5], 1, 3))
