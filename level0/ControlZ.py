# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer = 0

    letters = s.split()

    for index, word in enumerate(letters):
        if word == 'Z':
            continue
        else:
            if index + 1 == len(letters) and letters[index] != 'Z':
                answer += int(word)

            if index + 1 < len(letters) and letters[index + 1] != 'Z':
                answer += int(word)

    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))