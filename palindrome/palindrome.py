def is_palindrome(word):
    
    for i in range(len(word)//2):               # 0부터 문자열 길이의 절반만큼 반복
        if word[i] != word[len(word) - 1 - i]:  # i번째 인덱스와 반대쪽 인덱스의 값을 비교
            return False
    else:
        return True
        
        
# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))