# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1
# [S/W 문제해결 응용] 2일차 - 최대 상금
# D3

def solution_1244():
    n = int(input()) # a number of test cases
    test_cases = []
    
    for _ in range(n):
        num, change = map(int, input().split(" "))
        cards =list(map(int, str(num)))
        test_cases.append((cards, change))
    
    for i, tc in enumerate(test_cases):
        cards, change = tc 
        MAX = sorted(cards, reverse=True) # 카드로 구성할 수 있는 최댓값
        
        





            
# cards= [1,2,3,4]
# print(cards.index(max(cards)))
solution_1244()