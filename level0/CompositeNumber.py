#https://school.programmers.co.kr/learn/courses/30/lessons/120846


def solution(n):
    answer = 0
    count = 0
    for num in range(4, n + 1):
        # 1은 무조건이니 빼도 된다.
        for little in range(1, num + 1):
            if num % little == 0:
                count += 1
        if count >= 3:
            answer += 1
            count = 0

    return answer


def solution2(n):
    output = 0
    for i in range(4, n + 1):
        ## 2또는 3 을 약수로 가지는 4 이상의 숫자들 거르는 조건 들
        max = int(i ** 0.5) + 1
        for j in range(2, max):
            if i % j == 0:
                output += 1
                break
    return output

print(solution2(6))
print(solution2(15))