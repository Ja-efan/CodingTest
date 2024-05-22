# https://softeer.ai/practice/6288
# 금고털이
# Lv.2

import sys

input = sys.stdin.readline
print = sys.stdout.write

def solution():

    w, n = map(int, input().rstrip().split())
    metals = []
    for i in range(n):
        metals.append(list(map(int, input().rstrip().split())))

    metals = sorted(metals, key=lambda x:x[1])  # 금속의 무게당 가격을 기준으로 오름차순 정렬

    price = 0
    while w :
        metal = metals.pop()
        m = metal[0]
        p = metal[1]

        if w >= m :
            w -= m
            price += m*p
        else :
            price += w*p
            w = 0
    
    print("{}".format(price))
                   

solution()