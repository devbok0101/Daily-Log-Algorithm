import math

def solution(numer1, denom1, numer2, denom2):
    calculatedNumer1 = numer1 * denom2
    calculatedNumer2 = numer2 * denom1
    answerDenom = denom1 * denom2
    answerNumer = calculatedNumer1 + calculatedNumer2

    if answerDenom == answerNumer:
        return [1,1]

    gcd = math.gcd(answerNumer, answerDenom)

    if gcd == 1:
        return [answerNumer, answerDenom]

    while (answerDenom % gcd == 0
           and answerNumer % gcd == 0) :
        answerDenom = answerDenom / gcd
        answerNumer = answerNumer / gcd

    answer = [answerNumer, answerDenom]
    return answer


print(solution(2,4,2,4))