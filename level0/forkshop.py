def solution(n, k):
    serviceBeverage = n // 10

    def calculateCount(service, order):
        if order - service <= 0:
            return 0
        return order - service

    answer = (12000 * n) + (2000 * calculateCount(serviceBeverage, k))
    return answer

print(solution(10, 3))