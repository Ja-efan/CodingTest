# https://www.acmicpc.net/problem/20125
# 쿠키의 신체 측정
# Silver IV

import sys
input = sys.stdin.readline # input().rstrip().split()

def solution():
    N = int(input().rstrip())
    cookie = []
    for _ in range(N):
        row = input().rstrip()
        cookie.append(row)

    # 머리 찾기
    head = (0,0)
    for i in range(N):
        breaker = False
        for j in range(N):
            if cookie[i][j] == "*":
                head = (i,j)
                breaker = True
                break
        if breaker :
            break
    
    # 심장 
    heart = (head[0]+1, head[1])

    # 팔은 심장이 위치한 행(heart[0]에 가로로 존재
    left_arm = 0
    right_arm = 0
    for k in range(N):
        if cookie[heart[0]][k] == "*":
            if k > heart[1]:
                right_arm += 1
            elif k < heart[1] :
                left_arm += 1
    
    # 허리 
    waste = 0
    for m in range(heart[0]+1, N):
        if cookie[m][heart[1]] != "*":
            break
        # cookie[m][heart[1]] == "*"
        waste += 1
        

    # 몸통 가장 아래 좌표 
    left_leg = 0
    right_leg = 0
    for l in range(heart[0]+1, N):
        if cookie[l][heart[1]-1] == '*':
            left_leg += 1
        
        if cookie[l][heart[1]+1] == '*':
            right_leg += 1

    
    print(f"{heart[0]+1} {heart[1]+1}")
    print(f"{left_arm} {right_arm} {waste} {left_leg} {right_leg}")
          

solution()