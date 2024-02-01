## 문제 설명
스타벅스는 줄어든 매출 때문에 지점 하나를 닫아야 하는 위기에 처해 있다. 어떤 지점을 닫는 게 회사에 타격이 적을지 고민인데, 서로 가까기 붙어 있는 매장이 있으면, 그 중 하나는 없어져도 괜찮지 않을까 싶다.

사장님은 비서 고은이에게, 직선 거리가 가장 가까운 두 매장을 찾아서 보고하라는 임무를 주셨다.

고은이는 영업팀에서 매장들 좌표 위치를 튜플 리스트로 받아 왔다.
```
# 예시 tuple 리스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
```

튜플은 각 매장의 위치를 $x$, $y$좌표로 나타낸 것이다.
고은이가 사용하려는 함수 `closet_pair`는 이 좌표 리스트를 파라미터로 받고, 리스트 안에서 가장 가까운 두 매장을 `[(x1, y1), (x2, y2)]`형식으로 리턴한다.


참고로 고은이는 이미 두 좌표 사이의 거리를 계산해 주는 함수 `distance`를 써 놨는데,
함수 `distance`는 인풋으로 두 튜플을 받아서 그 사이의 직선 거리를 리턴해준다.


```
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기에 코드를 입력하세요.

# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
```
	
```
[(2, 3), (3, 4)]
```

---

## 나의 풀이
```
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    
    closest_store = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]
            if distance(closest_store[0], closest_store[1]) > distance(store1, store2):
                closest_store = [store1, store2]
                
    return closest_store

# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
```

나는 거리가 가장 가까운 두 매장을 담아두는 `closest_store`변수를 만들었고, `coordinates[0]`과 `coordinates[1]`을 기본값으로 저장했다.

```
    closest_store = [coordinates[0], coordinates[1]]
```

그리고 이제 반복문을 통해서 모든 경우의 수를 고려해야 하는데,
예를 들어, 첫 번째 매장을 기준으로 했을 때 두 번째 매장부터 비교를 시작하기 때문에
리스트의 총 길이에서 1만큼 뺀 횟수만큼 반복하게 된다.
그리고 중첩 반복문을 통해 첫 번째 매장이었던 기준을 두 번째, 세 번째로 옮겨가야 하기 때문에
`j`의 시작점을 `i`에 1을 더해줌으로써 해결할 수 있었다.

```
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
```


현재의 매장을 `store1`, `store2`에 각각 저장하고,
만약 현재 두 매장 사이의 거리가 가장 가까운 두 매장을 저장해뒀던 `closest_store`보다 크다면,
현재 두 매장을 `closest_store`에 저장시켜 업데이트 해주는 방식으로 구현하였다.


```
            store1, store2 = coordinates[i], coordinates[j]
            if distance(closest_store[0], closest_store[1]) > distance(store1, store2):
                closest_store = [store1, store2]
```


인풋 리스트 `coordinates`의 길이를 $n$이라고 했을 때,
함수 `closeset_pair`에는 반복문 두 개가 중첩되어 있는데, 둘 다 반복 횟수가 $n$에 비례한다.
따라서 함수의 시간 복잡도는 $O(n^2)$이다.




