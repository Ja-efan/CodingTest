# https://www.acmicpc.net/problem/2164
# 카드2
# Silver IV

import sys
from collections import deque
input = sys.stdin.readline
# input().rstrip().split()

def solution():

    N = int(input().rstrip())
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(2)
        return  
    
    cards = deque([i+1 for i in range(N)])

    while True:
        if len(cards) == 1:
            break
        cards.popleft()
        cards.append(cards.popleft())
    print(cards[0])

solution()