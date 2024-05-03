# 42584 
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격
# stack & queue

from collections import deque

def solution(prices:list) -> list:
    """
    주식 가격 :
    초 단위로 기록된 주식 가격이 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 반환하세요.

    Args :
    - prices : 초 단위로 기록된 주식 가격이 담긴 리스트 
        * prices의 각 가격은 1이상 10,000이하인 자연수 
        * prices의 길이는 2이상 100,000이하
    """

    # # solution 1 : O(n^2) -> 효율성 3번 시간초과  
    # prices = deque(prices)
    # seconds = []
    # while prices :
    #     p = prices.popleft()
    #     if not prices:
    #         seconds.append(0)
    #         break    
    #     count = 0
    #     for i in range(len(prices)):
    #         count += 1
    #         if p > prices[i]:
    #             break 
            
    #     seconds.append(count)


    # return seconds

    # solution 2 : O(n^2), 시간초과 없음 100/100
    seconds = []
    prices = deque(prices)
    while prices :
        p = prices.popleft()
        stack = []
        for p2 in prices:
            stack.append(p2)
            if p > p2 :
                break
        seconds.append(len(stack))
        
    return seconds 

# test case 
print(solution([1,2,3,2,3])) # [4,3,1,1,0]
print(solution([4,2,3,1])) # [1,2,1,0]