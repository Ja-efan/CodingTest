# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AY6cg0MKeVkDFAXt&categoryId=AY6cg0MKeVkDFAXt&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 공평한 분배 2
# D3

def solution_20728():
    t = int(input())
    for tc in range(1, t+1):
        n, k = map(int, input().split())
        candies = list(map(int, input().split()))
        candies = sorted(candies, reverse=True)
        diff_list = []
        for i in range(0,n-k+1):
            max_candies = candies[i:i+k][0]     
            min_candies = candies[i:i+k][-1]
            diff_list.append(max_candies-min_candies)
        
        print(f"#{tc} {min(diff_list)}")



solution_20728()