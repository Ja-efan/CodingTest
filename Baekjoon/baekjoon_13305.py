# https://www.acmicpc.net/problem/13305
# 주유소
# Silve III

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

def solution():
    N = int(input().rstrip())  # 도시의 개수 
    distance = list(map(int, input().rstrip().split()))  # 두 도시를 연결하는 도로의 길이 
    gas_stn = list(map(int, input().rstrip().split()))  # 주유소 가격 리스트
    gas_stn = deque(gas_stn)

    total_price = 0
    city = 0
    while True:
        if city == N-1:
            break
        price = gas_stn[city]
        next_city = city
        while price <= gas_stn[next_city]:
            if next_city== N-1:
                break
            next_city += 1
        # j번째 city가 정해짐, city=j
        dist = sum(distance[city:next_city])
        total_price += dist*price
        city = next_city
    
    print(str(total_price))

solution()