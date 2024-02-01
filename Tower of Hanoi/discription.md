## 문제 설명
하노이의 탑 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것이다.

![](https://velog.velcdn.com/images/b1uesoda/post/be119d3e-41f8-495d-9546-bb0cfafaa780/image.png)




지켜야할 규칙은 두가지이다.

1. 한 번에 하나의 원판만 옮길 수 있다.
2. 큰 원판이 작은 원판 위에 있어서는 안 된다.


하노이의 탑 게임의 해답을 출력해주는 함수 `hanoi`를 써라.
`hanoi`는 파라미터로 원판 수 `num_disks`, 게임을 시작하는 기둥 번호 `start_peg`, 그리고 목표로 하는 기둥 번호 `end_peg`를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력한다!

```
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 여기에 코드를 작성하세요

# 테스트 코드 (포함하여 제출해 주세요)
hanoi(3, 1, 3)

```

```
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동

```

가장 작은 원판의 번호는 1번이고 가장 큰 원판의 번호는 `num_disks`번이다.
그리고 왼쪽 기둥이 1번, 가운데 기둥이 2번, 오른쪽 기둥이 3번이다.


### 원판 하나인 경우
```
hanoi(1, 1, 3)
```

```
1번 원판을 1번 기둥에서 3번 기둥으로 이동
```


### 원판 두개인 경우
```
hanoi(2, 1, 3)
```
 
```
1번 원판을 1번 기둥에서 2번 기둥으로 이동
2번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 3번 기둥으로 이동

```

### 원판 세개인 경우
```
hanoi(3, 1, 3)
```

```
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동

```

---


## 나의 풀이
아직 나에겐 어려워서 고심 끝에 힌트를 보면서 풀었다..ㅎ
그래도 차근차근 다시 살펴보자!

```
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):

    if num_disks == 1:
        return move_disk(1, start_peg, end_peg)

    mid_peg = 6 - start_peg - end_peg
    
    hanoi(num_disks - 1, start_peg, mid_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, mid_peg, end_peg)
    
# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
```

일단 가장 쉬운 경우는 원판이 하나일 때이다.
원판이 하나일 때에는 1번 원판을 목적지 원판으로 이동시켜 주기만 하면 된다.

```
def hanoi(num_disks, start_peg, end_peg):

    if num_disks == 1:
        return move_disk(1, start_peg, end_peg)
```




원판이 2개인 경우는 조금 더 생각을 해야한다.
1번 원판을 1번 기둥에서 2번 기둥으로 옮기고, 2번 원판을 2번 기둥에서 3번 기둥으로 옮기고, 1번 원판을 2번 기둥에서 3번 기둥으로 옮기면 된다.

![](https://velog.velcdn.com/images/b1uesoda/post/e01eb498-2dc3-4377-bd46-27191ca2e994/image.png)








이제 원판이 3개인 경우이다.
![](https://velog.velcdn.com/images/b1uesoda/post/c12fa9b1-5f7b-46ca-b592-6b23bd310579/image.png)



일단 3번 원판이 3번 기둥에 가야하는데, 그러기 위해서는 1,2번 원판이 2번 기둥에 가있어야 한다.
원팬 2개를 옮기는 것은 위에서 했던 거에서 목적지가 3번에서 2번으로 바뀌었다는 점만 다르다.
방법은 `hanoi` 함수를 시작 기둥과 끝 기둥 인풋만 바꿔주고 재귀적으로 호출하면 된다!



![](https://velog.velcdn.com/images/b1uesoda/post/04ed7ef9-1682-4562-a7e1-7523a039e689/image.png)







이제 우리의 목표인 3번 원판을 3번 기둥으로 옮기면 된다.

![](https://velog.velcdn.com/images/b1uesoda/post/2ba9dff7-6d6e-466d-8a02-8a3fe1faae15/image.png)


마지막으로 2번 기둥에 있은 원판 2개를 3번 기둥으로 옮겨야 하는데,
이것도 위에서 했던 것과 똑같이 하면 된다. 유일한 차이는 이번에는 1,2번 원판을 2번 기둥에서 3번 기둥으로 옮겼다는 점이다.

![](https://velog.velcdn.com/images/b1uesoda/post/342b4b6f-3916-4794-b5cc-e42912ba4c02/image.png)



원판이 4개인 경우도 원판 3개인 경우랑 똑같이 생각할 수 있다.

4번 원판을 3번 기둥으로 옮기기 위해서 그 위에 원판 3개를 먼저 2번 기둥으로 옮겨야 한다.
원판 3개를 옮기는 것은 위에서 했던 방식 그대로 하면 된다.
![](https://velog.velcdn.com/images/b1uesoda/post/6f5e54e8-c03b-47fa-ad82-eca47affdbc3/image.png)


여기서 이제 4번 원판을 3번 기둥으로 옮기고

![](https://velog.velcdn.com/images/b1uesoda/post/21f0ef9d-f9c8-497d-bd2b-ef7e5192cad7/image.png)



다시 원판 3개를 3번 기둥으로 옮기면 끝이 난다.
![](https://velog.velcdn.com/images/b1uesoda/post/e31d00a8-513e-4fe5-b9e9-389ae22abd65/image.png)





매커니즘은 이제 이해했으니 알고리즘을 구현해 보자!




우선, 나는 2번 기둥을 `mid_peg`로 정의하였다.
기둥의 번호를 모두 더하면 항상 6이기 때문에, 6에서 나머지 기둥들을 뺀 값인 2가 중간 기둥이 되는 것이다.

```
    mid_peg = 6 - start_peg - end_peg

```

위에서 이해한 내용을 토대로 정리한 우리의 recursive case는 다음과 같다!


1. 가장 큰 원판을 제외하고 나머지 원판들을 `start_peg`에서 `mid_peg`로 이동

```
    hanoi(num_disks - 1, start_peg, mid_peg)
```





2. 가장 큰 원판을 `start_peg`에서 `end_peg`로 이동

```
    move_disk(num_disks, start_peg, end_peg)
```



3. 나머지 원판들을 `mid_peg`에서 `end_peg`로 이동

```
    hanoi(num_disks - 1, mid_peg, end_peg)
```

---
재귀 함수를 공부하게 되면 누구나 거치게 된다는 하노이의 탑 문제..
원리를 알고 나면 이해가 되는데, 막상 코드로 옮기려고 하니까 잘 안된다😂

   






