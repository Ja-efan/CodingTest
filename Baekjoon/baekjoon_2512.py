# https://www.acmicpc.net/problem/2512
# 예산
# Silver II

import sys

input = sys.stdin.readline
output = sys.stdout.write

def solution():
    N = int(input())
    b_requests = list(map(int, input().split()))
    B = int(input())

    answer = 0
    if sum(b_requests) <= B :
        answer = str(max(b_requests))

    else : # sum(b_requests) > B
        b_requests.sort()  # 오름차순 정렬
        min_ = 0
        max_ = max(b_requests)

        while min_ <= max_:
            total  = 0 
            mid = (min_ + max_) // 2        
            for b in b_requests:
                total += min(mid, b)
            if total <= B:
                min_ = mid + 1
                answer = mid
            else :
                max_ = mid - 1

    output(str(answer))


solution()