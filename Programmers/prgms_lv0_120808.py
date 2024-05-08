# https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 분수의 덧셈

def solution(numer1:int, denom1:int, numer2:int, denom2:int) -> list :
    denom = denom1 * denom2 
    numer = numer1 * denom2 + numer2 * denom1
    for i in range(denom, 0, -1):
        a = divmod(numer,i)
        b = divmod(denom , i)
        if a[1] == 0 and b[1] == 0 :
            return [a[0], b[0]]
        
# test case
print(solution(1,2,3,4)) # [5,4]
print(solution(9,2,1,3)) # [29,6]