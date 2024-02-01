

## 문제 설명
합병 정렬 알고리즘 중 사용되는 `merge` 함수를 작성하라!
`merge` 함수는 정렬된 두 리스트 `list1`과 `list2`를 받아서, 하나의 정렬된 리스트를 리턴한다.

```
def merge(list1, list2):
   

# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

```
```
[1]
[1]
[1, 2]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 3, 4, 6, 7, 8, 9, 10]
```



---
## 나의 풀이
```
def merge(list1, list2):
 
	merged_list = []
    
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if i == len(list1):
        merged_list += list2[j:]

    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list

# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

```


일단 처음에는 `merged_list`를 빈 리스트로 정의해 주었다.
```
	merged_list = []
```

`list1`과 `list2`는 이미 정렬되어 있기 때문에, 두 리스트 중 더 작은 값을 `merged_list`에 차곡차곡 추가해야 한다.

```
def merge(list1, list2):
 
	merged_list = []
    
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
```

그래서 나는 이렇게 while문을 통해서 `i`와 `j`를 각각 `list1`과 `list2`의 인덱스로 두고, `list1`의 `i`번째 요소가 `list2`의 `j`번째 요소보다 크다면 `merged_list`에 더 작은 값인 `list2`의 값을 추가시켜 주었다.
다음 반복 시에는 `list2`의 다음 요소를 비교해야 하기 때문에, `j`를 $1$만큼 증가시켜 주었다.

반대인 경우 즉, `list1`의 값이 `list2`의 값보다 작을 때는 `list1`의 값을 `merged_list`에 넣고, `i`를 $1$만큼 증가시켜 주었다.


하지만 여기서 끝이 아니다.

만약 한 쪽 리스트가 다 소진되었을 때, 다른 한 쪽 리스트의 값들을 `merged_list`에 순차적으로 넣어줘야 한다.

그것을 해결하기 위해서 조건문을 통해 다 소진되지 않은 리스트가 어느 것인지 먼저 판단해 주었다.
위의 반복문에서 `i`가 계속 증가하다가 리스트의 길이와 `i`가 같아지게 되면 그 리스트는 모두 다 소진되었다는 의미이다.

```
    if i == len(list1):
        merged_list += list2[j:]

    elif j == len(list2):
        merged_list += list1[i:]
```        

`i`나 `j`중 하나가 리스트의 길이와 같아졌다면,
다른 리스트의 남은 요소들을 그대로 `merged_list`에 넣어주면 merge작업이 끝이 난다.


```
    return merged_list
```
최종적으로 `merged_list`를 반환해줌으로써 문제를 해결할 수 있다!

