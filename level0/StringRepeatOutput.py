# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    return ''.join(string * n for string in my_string)

print(solution('hello', 3))