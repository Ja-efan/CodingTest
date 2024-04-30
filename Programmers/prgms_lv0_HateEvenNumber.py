# 120813 
# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n:int) : 
    answer = []
    for i in range(n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer

# test case 
print(solution(10)) # [1, 3, 5, 7, 9]
print(solution(15)) # [1, 3, 5, 7, 9, 11, 13, 15]