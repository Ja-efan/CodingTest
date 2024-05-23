# https://www.acmicpc.net/problem/21921
# 블로그
# Silver III

import sys
from collections import defaultdict

input = sys.stdin.readline
output = sys.stdout.write

def solution(): # time out

    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))

    max_dict = defaultdict(int)
    max_visitors = 0
    
    for i in range(N-X+1):
        summ = sum(visitors[i:i+X])
        if max_visitors <= summ:
            max_dict[summ] += 1
            max_visitors = summ

    if max_visitors == 0:
        output("SAD")
    else :
        output(str(max_visitors)+'\n')
        output(str(max_dict[max_visitors]))
        

solution()