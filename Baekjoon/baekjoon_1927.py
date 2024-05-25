# https://www.acmicpc.net/problem/1927
# 최소 힙
# Silver II


import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

def solution():

    N = int(input())
    arr = []
    heapq.heapify(arr)
    for _ in range(N):
        x = int(input())
        if x == 0: # 배열에서 가장 작은 값을 출력 
            if not arr:
                output(str(0)+'\n')
            else :
                output(str(heapq.heappop(arr))+'\n')
        else :
            heapq.heappush(arr, x)

solution()
