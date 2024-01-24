# 문제 설명

"토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 palindrome이라고 부른다. 문자열 word가 palindrome인지 확인하는 함수 is_palindrome을 만들어라! is_palindrome은 word가 palindrome이면 True를, palindrome이 아니면 False를 리턴한다.


```
def is_palindrome(word):
    # 여기에 코드를 작성하세요
    

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

```
```
True
False
True
True
False
```



"racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 하고, "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 한다.