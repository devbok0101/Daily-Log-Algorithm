## 접근 방법 생각하기

1. n개의 퀸
2. n * n 의 보드
3. 퀸은 8방향으로 공격 가능
4. n = 2 일 경우, 퀸을 놓을 수 없을 때 답은 []
5. 제약 조건 확인 결과 1<= n <= 9
   6. n의 제곱이 되더라도 10의 8제곱 넘을 수 없음
   7. 시간 복잡도 O의 제곱으로 풀어도 오케이
   8. 백트래킹 해야할것으로 보임


1. n*n 보드 만들기
2. (0,0)부터 시작할거고
3. (1,1) 기준으로 했을 때 8방으로 움직이려면 아래와 같고 n을 넘어서는 안되겠지

```
[
  (-1, -1), (-1.0), (-1,1)
  (0,-1),         (0,1)
  (1, -1)  (1, 0)  (1,1)        
]

```

라고 생각 했으나, 다른 방법으로 풀 수 있었음!
반복문을 통해서, 왼쪽 대각선, 오른쪽 대각선을 검색한다.

```python

n = 4

board = [["." for _ in range(n)] for _ in range(n)]

["".join(row) for row in board]

result = [["....", "....", "....", "...."]]

```



