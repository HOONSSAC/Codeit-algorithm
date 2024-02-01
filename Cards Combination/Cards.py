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