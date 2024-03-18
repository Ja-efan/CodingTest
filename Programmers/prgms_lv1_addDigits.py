"""
https://school.programmers.co.kr/learn/courses/30/lessons/12931
"""
def solution(n:int)-> int:
    n_str = str(n)
    answer = 0
    for i in range(len(n_str)):
        answer = answer + int(n_str[i])
    return answer 

print(solution(123))