## 문제 접근 방법 생각하기

1. answer 정답을 담을 리스트 생성 [0,0,0 ... n]
2. stack 형태로 temperatures를 담는다 뒤에서 부터
   3. stack은 LIFO
4. temperature[0] 부터 해서 카운트 하기 넘었는지 안넘었는지 체크
5. 넘었다? 해당 숫자는 answer[0] 값 변경해주기