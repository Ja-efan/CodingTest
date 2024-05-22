# https://softeer.ai/practice/6294
# 성적 평균
# Lv.3

import sys

input = sys.stdin.readline
print = sys.stdout.write

def solution():
    n, k = map(int, input().rstrip().split())
    scores = list(map(int, input().rstrip().split()))
    ranges = []
    for _ in range(k):
        ranges.append(list(map(int, input().rstrip().split())))

    for r in ranges:
        a = r[0]
        b = r[1]
        summ = 0
        for s in scores[a-1:b]:
            summ += s
        avg = round((summ / (b-a+1)), 2)

solution()

"""
5 3
10 50 20 70 100
1 3
3 4
1 5
"""