# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AY4XhKTKU0IDFARM&categoryId=AY4XhKTKU0IDFARM&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 증가하는 사탕 수열
# D3

def solution_20551():
    t = int(input())
    for tc in range(1,t+1):
        candies = list(map(int, input().split()))
        cnt = 0
        if candies[2] <= candies[1]:
            cnt += candies[1] - candies[2] + 1
            candies[1] = candies[1] - cnt
            
        if  candies[1] <= candies[0]:
            cnt += candies[0] - candies[1] + 1
            candies[0] -= (candies[0] - candies[1] + 1)

        if 0 in candies:
            print(f"#{tc} {-1}")
        else:
            print(f"#{tc} {cnt}")

solution_20551()