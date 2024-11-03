## 문제 접근 방법 생각하기

1. answer 정답을 담을 리스트 생성 [0,0,0 ... n]
2. stack 형태로 temperatures를 담는다 뒤에서 부터
   3. stack은 LIFO
4. temperature[0] 부터 해서 카운트 하기 넘었는지 안넘었는지 체크
5. 넘었다? 해당 숫자는 answer[0] 값 변경해주기


## 설계를 이렇게 하라고 한다.

1. temperatures 배열의 처음부터 순회해서 answer 채우기
2. 스택의 마지막 온도가 현재 temperature 인덱스 온도보다 작으면
   3. 스택이 비거나, 스택 마지막 온도가 현재 온도보다 커질 때까지 pop
   4. 현재 온도 인덱스와 스택에 저장해둔 인덱스 차이로 answer 값 구하기
5. 스택에 현재 temperatures의 인덱스와 그온도 저장