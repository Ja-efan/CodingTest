# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
# 백만 장자 프로젝트 
from collections import deque
def solution_1859():
    t = int(input()) # a number of test case
    test_cases = []
    for _ in range(t):
        n = int(input()) 
        # for _ in range(n):
        test_cases.append(map(int, input().split(" ")))

    # return_str = ""
    # use stack 
    for i,prices in enumerate(test_cases):
        prices = deque(prices)
        answer = 0
        while prices:
            p = prices.pop()
            while prices and p >= prices[-1]:
                p2 = prices.pop()
                answer += (p - p2)
        print(f"#{i+1} {answer}")
    

solution_1859()