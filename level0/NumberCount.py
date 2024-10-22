# https://school.programmers.co.kr/learn/courses/30/lessons/120824


def solution(num_list):
    answer = []

    even_num_count = 0
    odd_num_count = 0

    for num in num_list:
        if num % 2 == 0:
            even_num_count += 1
        else:
            odd_num_count += 1

    answer = [even_num_count, odd_num_count]

    return answer


print(solution([1, 2, 3, 4, 5]))
