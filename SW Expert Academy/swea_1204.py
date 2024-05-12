# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=1
# [S/W 문제해결 기본] 1일차 - 최빈수 구하기 
# D2

# Memroy Error 
def solution_1204():
    # from collections import deque 

    t = int(input())
    test_cases = []
    for _ in range(t):
        _ = input()
        test_cases.append(list(map(int, input().split(" "))))
    
    for i, tc in enumerate(test_cases):
        counter = [0 for _ in range(101)]
        for n in tc:
            counter[n] += 1
            breaker = False
            if counter[n] > len(tc)//2:
                print(f"#{i+1} {n}")
                breaker = True
                break
        if breaker == True:
            continue
        max_ = 0
        for j in range(len(counter)):
            if counter[j] >= counter[max_]:
                max_ = j
        print(f"#{i+1} {max_}")

# Memory Error 
def solution_1204_2():
    t = int(input())
    for i in range(1, t+1):
        tc_num = int(input())
        tc = list(map(int, input().split(" ")))
        counter = [0 for _ in range(101)]
        for n in tc:
            counter[n] += 1
        max_ = 0
        for j in range(len(counter)):
            if counter[j] >= counter[max_]:
                max_ = j
        print(f"#{i} {max_}")

# Passed
def solution_1204_3():
    T = int(input())
    for i in range(1, T+1):
        TN = int(input())
        scores = list(map(int, input().split())) 
        scores_dict = dict()
        for score in scores:
            if score in scores_dict.keys():
                scores_dict[score] += 1
            else :
                scores_dict[score] = 1
        
        max_k = 0
        max_v = 0
        for k, v in scores_dict.items():
            if v > max_v :
                max_v = v 
                max_k = k
            elif v == max_v and k > max_k :
                max_v = v 
                max_k = k
        print(f"#{i} {max_k}")

solution_1204_3()


