#https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    answer = 0
    for word in my_string:
        if word.isdigit():
            answer += int(word)
    return answer

print(solution("aAb1B2cC34oOp"))