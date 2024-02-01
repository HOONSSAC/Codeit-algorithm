## 문제 설명

카드 두 뭉치가 있다.

왼쪽 뭉치에서 카드를 하나 뽑고, 오른쪽 뭉치에서 카드를 하나 뽑아서, 두 수의 곱이 가장 크게 만들고 싶다. 어떻게 하면 가장 큰 곱을 구할 수 있을까?

함수 `max_product`는 리스트 `left_cards`와 리스트 `right_cards`를 파라미터로 받는다.
`left_cards`는 왼쪽 카드 뭉치의 숫자들, `right_cards`는 오른쪽 카드 뭉치 숫자들이 담겨 있고, `max_product`는 `left_cards`에서 카드 하나와 `right_cards`에서 카드 하나를 뽑아서 곱했을 때 그 값이 최대가 되는 값을 리턴한다.

```
def max_product(left_cards, right_cards):
    # 여기에 코드를 작성하세요

# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

```


```
24
32
28
```


---

## 나의 풀이
```
def max_product(left_cards, right_cards):
    
    output = 0
    
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            new_output = left_cards[i] * right_cards[j]
            if new_output > output:
                output = new_output
    
    return output
    
# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

```

나는 우선 최종 리턴 변수로 `output`을 지정했다.
그리고 이중 반복문을 통하여 두 카드 뭉치의 모든 경우의 수를 완전탐색(Brute Force)하였다.
`new_ouput`에다가 현재 내가 뽑은 두 카드의 곱을 입력하고 만약 그 값이 현재의 `output`보다 크다면, 해당 값을`output`에다가 업데이트 해주는 방식으로 접근하였다.

`len(left_cards)`을 $m$, `len(right_cards)`을 $n$이라고 했을 때,
함수 `max_product`의 시간 복잡도는 $O(mn)$이다.