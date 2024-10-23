# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''

    for str in my_string:
        str = str * n
        answer += str

    return answer

print(solution('hello', 3))