# https://www.acmicpc.net/problem/1138
# 한 줄로 서기 
# Silver II

import sys

inputf = sys.stdin.readline
printf = sys.stdout.write

def solution():
    N = int(inputf())
    arr = list(map(int, inputf().rstrip().split()))
    line = [0 for _ in range(N)]

    for i in range(N):
        count = 0 
        num = arr[i]
        j = 0
        while True:
            if line[j] == 0 and count == num:
                line[j] = i+1
                break

            if line[j] == 0 :
                count += 1
            
            j += 1

    print(*line, end=" ")


solution()
        
            