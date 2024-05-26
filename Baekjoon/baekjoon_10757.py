# https://www.acmicpc.net/problem/10757
# 큰 수 A+B
# Bronze V

import sys

input = sys.stdin.readline
output = sys.stdout.write

def solution():
    a, b = map(int, input().split())
    output(str(a+b))

solution()