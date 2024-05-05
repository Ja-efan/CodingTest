# https://school.programmers.co.kr/learn/courses/30/lessons/12927
# 야근 지수
"""
    야근 지수 :
    1시간 동안 작업량을 1만큼을 처리할 수 있다고 할 때, 
    퇴근 까지 남은 n 시간과 각 일에 대한 작업량 works에 대해야근 피로도를 최소화한 값을 반환
    (야근 피로도 : 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값)

    Args :
    - works : 길이 1이상 20,000이하인 배열, 각 원소는 50,000 이하인 자연수 
    - n : 1,000,000 이하인 자연수 

"""
# solution 1 : 효율성 1,2 시간초과 
# def solution(n:int, works:list) -> int:
    # import numpy as np

    # for _ in range(n):
    #     maxx = max(works) # 가장 많이 남은 작업량
    #     maxx_idx = np.argmax(works)
    #     if works[maxx_idx] == 0 :
    #         break
    #     works[maxx_idx] -= 1
    
    # yagun = 0
    # for i in works:
    #     yagun += i**2
    # return yagun

# # solution 2 : 효율성 1,2 시간초과 
# def solution(n:int, works:list) -> int:
#     for _ in range(n):
#         if max(works) == 0 :
#             break
#         works = sorted(works, reverse=True)
#         works[0] -= 1

#     yagun = 0
#     for i in works:
#         yagun += i**2
#     return yagun 

# solution 3 
def solution(n:int, works:list) -> list :
    import heapq
    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        if works[0] == 0 :
            break
        heapq.heapreplace(works, works[0]+1)
    yagun = 0
    for i in works:
        yagun += i**2
    return yagun 

# test case 
print(solution(4, [4,3,3])) # 12
print(solution(1, [2,1,2])) # 6
print(solution(3, [1,1])) # 0
print(solution(999, [800, 100, 55, 45])) # 1

