

## 문제 설명
Divide and Conquer를 이용해서 $1$부터 $n$까지 더하는 함수를 만들어 보자!

우리가 작성할 함수 `consecutive_sum`은 두 개의 정수 인풋 `start`와 `end`를 받고, `start`부터 `end`까지의 합을 리턴한다. `end`는 `start`보다 크다고 가정하자.


---


## 나의 풀이
```
def consecutive_sum(start, end):
    if start == end:
        return start
        
    return consecutive_sum(start, (start + end) // 2) + consecutive_sum((start + end) // 2 + 1, end)

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
```

```
55
5050
32131
75466
```


예를 들어,
1~10의 합을 1~5의 합과 6~10의 합으로
1~5의 합은 또 다시 1~2의 합과 3~5의 합으로
Divide를 반복해주면 된다.

그리고 재귀 함수를 통해 Conquer과정을 반복하면서
`start`와 `end`가 같아졌을 때는 `start`를 리턴해주면 된다.

```
def consecutive_sum(start, end):
    if start == end:
        return start
```

마지막으로 재귀적으로 구한 값들을 Combine해서 리턴해주면 된다!
```
    return consecutive_sum(start, (start + end) // 2) + consecutive_sum((start + end) // 2 + 1, end)
```





