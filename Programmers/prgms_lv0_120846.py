# https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 합성수 찾기 

def solution(n:int) -> int:
    # 약수의 개수가 3개 이상이려면 최소 4부터 시작해야 한다.
    answer = 0
    for i in range(4, n+1) : 
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count >= 3 :
            answer += 1
    
    return answer 

# test case 
print(solution(10)) # 5
print(solution(15)) # 8