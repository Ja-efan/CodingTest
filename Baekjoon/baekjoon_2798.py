# 2798
# 블랙잭
# https://www.acmicpc.net/problem/2798

import itertools
from itertools import combinations

n,m = map(int, input().split(' '))
cards_str = input().split(' ')
cards = []
for i in range(len(cards_str)):
    cards.append(int(cards_str[i]))
comb = combinations(cards, 3)
summ_list = []
for c in comb:
    summ_list.append(sum(c))
result = 0
for i in summ_list:
    if i > result and i <= m:
        result = i
print(result)
    


