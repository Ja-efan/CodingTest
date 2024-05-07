# https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 저주의 숫자 3

def solution(n:int) -> int :
    threex = 0
    for i in range(1, n+1):
        threex += 1
        while threex % 3 == 0 or '3' in str(threex):
            threex += 1
    
    return threex


# test case 
print(solution(15)) # 25
print(solution(40)) # 76
