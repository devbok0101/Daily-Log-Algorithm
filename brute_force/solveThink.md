
https://school.programmers.co.kr/learn/courses/30/lessons/86491

* for 문하는것 익숙해지기

* 아래는 N차원 배열일 때 최대값 찾기
```python3


sizes = [[5,7], [8,9]]
max_value = max(size[0] for size in sizes)
print(max_value) // 8

```


* N 차원 배열일 때 큰 값으로 위치 바꿔주기
```python


sizes = [[5,7], [8,9]]
for i in range(len(sizes)):
    sizes[i] = sorted(sizes[i], reverse = True)
    
#answer = [[7, 5], [9, 8]]

```