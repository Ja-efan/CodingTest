# https://www.acmicpc.net/problem/11501
# 주식
# Silver II

import sys
from collections import deque

inputf = sys.stdin.readline
printf = sys.stdout.write

def solution():

    T = int(inputf())

    for tc in range(1, T+1):
        N = int(input())
        stocks = list(map(int, input().split()))
        stocks = deque(stocks)
        
        profit = 0

        while stocks:
            stock = stocks.pop()
            while stocks and stocks[-1] <= stock:
                buying = stocks.pop()
                profit += stock - buying
        

        printf(str(profit)+'\n')

solution()