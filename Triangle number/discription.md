# 문제 설명
---
n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합이다.
파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해 주는 재귀 함수 triangle_number를 써라.
n은 1이상의 자연수라고 가정하자.

단, 함수 안에 반복문은 쓰면 안된다!
---
```
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # 여기에 코드를 작성하세요

# 테스트 코드: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))
```

```
1
3
6
10
15
21
28
36
45
55
```